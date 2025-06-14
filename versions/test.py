import pyautogui as py
import os
import time

waifu_dir = 'waifus'
tempo_de_espera = 10  # segundos para esperar se não encontrar nenhuma

def encontrar_imagem(imagem_path):
    try:
        caminho = os.path.join(waifu_dir, imagem_path)
        posicao = py.locateCenterOnScreen(caminho, confidence=0.8)
        if posicao:
            print(f'✅ Waifu encontrada: {imagem_path}')
            return True
    except Exception:
        print(f'❌ Waifu não encontrada: {imagem_path}')
        return False

while True:
    print('\n🔍 Procurando alguma waifu na tela...')
    encontrou_alguma = False

    imagens = os.listdir(waifu_dir)
    for imagem in imagens:
        if encontrar_imagem(imagem):
            encontrou_alguma = True
            break  # Se encontrou uma, para o loop

    if encontrou_alguma:
        print('\n🎯 Waifu encontrada! Interrompendo busca.\n')
        break  # Encerra o script se achou
    else:
        print(f'\n⏳ Nenhuma imagem encontrada. Esperando {tempo_de_espera} segundos antes de tentar novamente...\n')
        time.sleep(tempo_de_espera)
