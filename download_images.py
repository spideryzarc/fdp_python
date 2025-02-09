import os
import re
import sys
import requests
import hashlib
from urllib.parse import urlsplit, unquote

# Verifica se o parâmetro -y foi passado
yes_to_all = "-y" in sys.argv

if len(sys.argv) < 2:
    print("Uso: python script.py <arquivo.md>")
    sys.exit(1)

# Caminho do arquivo Markdown passado como argumento
md_file_path = sys.argv[1] if not yes_to_all else sys.argv[2]

# Pasta onde as imagens serão salvas
images_dir = "images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

def download_image(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
    except Exception as e:
        print(f"Falha ao baixar {url}: {e}")
        return None

    # Extrai o nome do arquivo da URL
    path = urlsplit(url).path
    filename = os.path.basename(path)
    filename = unquote(filename)
    if not filename:
        filename = "imagem.jpg"
    
    local_path = os.path.join(images_dir, filename)
    
    # Adiciona um hash da URL ao nome do arquivo para garantir unicidade se o arquivo já existir
    if os.path.exists(local_path):
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
        filename, ext = os.path.splitext(filename)
        filename = f"{filename}_{url_hash}{ext}"
        local_path = os.path.join(images_dir, filename)
    
    with open(local_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f"Imagem baixada: {url} -> {local_path}")
    return local_path.replace("\\", "/")

# Lê o conteúdo do arquivo Markdown
with open(md_file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Expressão regular para encontrar a sintaxe de imagem Markdown: ![texto](url)
pattern = r'(!\[[^\]]*\]\()([^\)]+)(\))'

def process_match(match):
    inicio, url, fim = match.groups()
    if url.startswith("http://") or url.startswith("https://"):
        print(f"\nImagem encontrada: {url}")
        if yes_to_all:
            escolha = 's'
        else:
            escolha = input("Deseja substituir essa imagem por uma cópia local? [s/n]: ").strip().lower()
        if escolha == 's':
            local_filename = download_image(url)
            if local_filename:
                return f"{inicio}{local_filename}{fim}"
    return match.group(0)

# Atualiza o conteúdo do Markdown com os novos links conforme decisão do usuário
new_content = re.sub(pattern, process_match, content)

# Sobrescreve o arquivo Markdown com as alterações
with open(md_file_path, "w", encoding="utf-8") as file:
    file.write(new_content)

print("\nArquivo Markdown atualizado com os links de imagem (se substituídos).")