import serial
import time

def send_number_to_analog_port(number, port, baudrate=9600):
    try:
        arduino = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Дадим ардуино время для инициализации

        data_to_send = f"<{number}>"
        arduino.write(data_to_send.encode())  # Отправляем данные в формате "<Данные>" на ардуино
        arduino.flush()  # Принудительно отправляем данные на ардуино
        response = arduino.readline().decode().strip()  # Читаем ответ от ардуино
        arduino.close()

        if response.startswith("SUCCESS:"):
            sent_number = int(response[len("SUCCESS:"):])
            if sent_number == number:
                print(f"Число {number} успешно отправлено на аналоговый порт пина 6 Arduino.")
            else:
                print(f"Ошибка: Ардуино сообщила о неправильно отправленном числе.")
        else:
            print("Ошибка: Ардуино не отправила подтверждение о выполнении.")

    except Exception as e:
        print(f"Ошибка при отправке числа на аналоговый порт пина 6 Arduino: {e}")

if __name__ == "__main__":
    number_to_send = 128  # Здесь замените на нужное вам число (от 0 до 255)
    serial_port = "COM3"  # Здесь укажите правильный порт, на котором подключена Arduino

    send_number_to_analog_port(number_to_send, serial_port)
