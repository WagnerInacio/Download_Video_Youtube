from pytube import YouTube

# Lista para armazenar os links dos vídeos
links = []

# Pergunta quantos links o usuário deseja inserir
num_links = int(input("Quantos links deseja inserir: "))

# Loop para inserção dos links
for i in range(num_links):
    links.append(input(f"Digite o link do vídeo {i + 1}: "))

# Diretório para salvar os vídeos
path = input("Digite o diretório que deseja salvar os vídeos: ")

# Loop para processamento de cada link
for link in links:
    yt = YouTube(link)

    # Mostra os detalhes do vídeo
    print("Título: ", yt.title)
    print("Número de views: ", yt.views)
    print("Tamanho do vídeo: ", yt.length, "minutos")
    print("Avaliação do vídeo: ", yt.rating)

    # Usa a maior resolução
    ys = yt.streams.get_highest_resolution()

    # Começa o download do vídeo
    print("Baixando...")
    ys.download(path)
    print("Download completo!")
