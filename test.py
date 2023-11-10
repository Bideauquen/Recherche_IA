from ocropy import ocr

# Charger l'image
image_path = 'page_1.jpg'
img = ocr.read_image(image_path)

# Effectuer l'OCR
resultats_ocr = ocr.recognize(img)

# Afficher les résultats
for resultat in resultats_ocr:
    print(resultat.text)
