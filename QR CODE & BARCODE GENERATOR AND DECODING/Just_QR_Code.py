import qrcode
from pyzbar.pyzbar import decode
import cv2
import os


# QR code
def create_qr_code(data, filename):
    # Ensure the directory exists
    if not os.path.exists('qr_codes'): # qr_codes- filename
        os.makedirs('qr_codes')

    qr = qrcode.QRCode(
        version=1, # for small size
        error_correction=qrcode.constants.ERROR_CORRECT_L, # (10% less data corupted ensuring)
        box_size=10, # qr code size
        border=4,
    )
    
    qr.add_data(data) # adjust to QRCode and given Date 
    qr.make(fit=True) # data fit to QRCode

    img = qr.make_image(fill="black", back_color="white") # make image
    
    # Save the QR code image
    img.save(f"qr_codes/{filename}.png")
    print(f"QR Code saved as qr_codes/{filename}.png")
    
    

# QR de-code
def decode_qr_code(filepath):
    # Decode QR Code
    img = cv2.imread(filepath) # img reading method
    decoded_objects = decode(img) # decode img
    for obj in decoded_objects: # seperate by data from image
        print(f"QR Code Data: {obj.data.decode('utf-8')}") # endcoing UTF-8 use for data extraing 



# main
def main():
    while True:
        # Ask user for choice
        print("\nChoose an option:")
        print("1. Create QR Code")
        print("2. Decode QR Code")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Take Student ID and Name
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            student_age = input("Enter Student Age: ")

            # Combine ID and Name
            data = f"- {student_id}\n All details \n - {student_name}\n - {student_age}"
            filename = student_id  # Use student ID as filename

            # Create QR Code
            create_qr_code(data, filename)

        elif choice == '2':
            # Decode QR Code
            filename = input("Enter the filename of the QR code (without extension): ") # take file name
            filepath = f"qr_codes/{filename}.png" # make file path
            
            if os.path.exists(filepath): # when filepath is exist
                print("\nDecoding QR Code:") # formal massafe
                decode_qr_code(filepath)  # asign 1st this line 
            else:
                print("QR code file not found.") # error handaling 

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice..")

if __name__ == "__main__":
    main()
