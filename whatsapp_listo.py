import pywhatkit
import pyautogui
import time
import os

carpeta_cliente = r"C:\Users\ruta..."
DATOS_ENVIO = {
    "telefono" : "+000000000",
    "ruta" : os.path.join(carpeta_cliente, "Logotipo OK JCG.jpg"),
    "mensaje" :"Estamos activos"
    }

def pulir_envio():
    if not os.path.exists(DATOS_ENVIO["ruta"]):
        print(f"Error: No se encuentra la imagen en {DATOS_ENVIO["ruta"]}")
        return

    print (f"Iniciando envío para {DATOS_ENVIO['telefono']}...") 

 
 

    try:
            pywhatkit.sendwhats_image(
                DATOS_ENVIO["telefono"], 
                DATOS_ENVIO["ruta"], 
                DATOS_ENVIO["mensaje"], 
                50
                )
            time.sleep(10)
            print("Trayendo ventana al frente...")
            pyautogui.hotkey("alt", "tab")
            time.sleep(2)
            print("Pegando imagen y enviando...")
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")
            print("Misión cumplida! Todo enviado con éxito.")

    except Exception as e: 
            print(f"Ocurrio un error: {e}")

if __name__ == "__main__":

    pulir_envio()