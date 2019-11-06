''' Class Conexion, aqui esta la conexion y los metodos para poder conectar a la base de datos '''
import sqlite3


class Conexion_bd:

    conexion = sqlite3.connect('cajero_bd')
    cursor = conexion.cursor()

    def insertar_usuario(self, nombre, apellido_1, apellido_2, dni):
        self.cursor.execute(f'''
        INSERT INTO "usuarios" (apellido_1, apellido_2, dni, nombre)
        VALUES
          (
            "{apellido_1}",
            "{apellido_2}",
            "{dni}",
            "{nombre}"
          )
        ''')
        # Guardar datos
        self.conexion.commit()
        # Cerrar conexion
        self.conexion.close()

    def leer_usuario(self, dni):
        self.cursor.execute(f''' 
        SELECT * FROM usuarios WHERE dni = "{dni}"
        ''')
        usuario = self.cursor.fetchall()
        # Guardar datos
        self.conexion.commit()
        # Cerrar conexion
        self.conexion.close()
        return usuario

    def get_dinero(self, dni):
        self.cursor.execute(f'''
        SELECT saldo FROM cuentas WHERE dni = "{dni}"
        ''')
        dinero = self.cursor.fetchall()
        # Guardar datos
        self.conexion.commit()
        # Cerrar conexion
        self.conexion.close()
        return dinero

    def set_dinero(self, dni, cantidad):
        self.cursor.execute(f'''
        UPDATE cuentas SET saldo = {cantidad} WHERE dni = "{dni}"
        ''')
        # Guardar datos
        self.conexion.commit()
        # Cerrar conexion
        self.conexion.close()