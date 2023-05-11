import datetime
import numpy as np
import time
from playsound import playsound

hora = datetime.datetime.now()
hora_actual = hora.strftime("%H:%M:%S")
other="SI"

print("¡BIENVENID@! vamos a configurar tu alarma, comencemos...\n")
print(f"En este momento la hora actual es: {hora_actual}\n")

d1=datetime.datetime.strptime(hora_actual,"%H:%M:%S")
h= np.int_(d1.hour)
m=np.int_(d1.minute)

while other == ("SI") and ("NO"):

    tiempo = input("Indique dentro de cuanto tiempo quiere que suene la alarma, por ejemplo '01:30:00': ")

    try:
        d2=datetime.datetime.strptime(tiempo,"%H:%M:%S")
        h_i= np.int_(d2.hour)
        m_i= np.int_(d2.minute)
        s_i= np.int_()

        alarma_h = (h + h_i + (m+m_i)//60) % 24
        alarma_m = (m + m_i) % 60

        print(f"\nLa alarma sonará a las {alarma_h:02}:{alarma_m:02} horas.")
        time.sleep(int((h + h_i + (m+m_i)//60) % 2)+int((m + m_i) % 60))

        cont=0
        while cont <= 2:
            print("\n¡ ¡ ¡  L A  A L A R M A  E S T A  S O N A N D O  ! ! !")
            playsound('C:/Users/Christian Fernandez/Documents/GitHub/Alarma.py/alarma.mp3')
            cont += 1
        break

    except ValueError:
        print("Recuerde ingresar el tiempo como en el ejemplo 'HH:MM:SS'\n")
        other = input("Desea volver a ingresar un timepo para la alarma? si / no: ").upper()

print("\nGracias por utilizar la alarma de python.")


