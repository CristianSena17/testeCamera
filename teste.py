import cv2
from picamera2 import Picamera2

# Inicializa a câmera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)  # Ajuste a resolução conforme necessário
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

while True:
    frame = picam2.capture_array()  # Captura o frame da câmera
    cv2.imshow("Camera", frame)  # Exibe o frame
    
    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
