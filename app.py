from flask import Flask, jsonify, request
from db_config import get_db_connection

app = Flask(__name__)


# Registrar un nuevo inmueble
@app.route("/inmuebles", methods=["POST"])
def registrar_inmueble():
    data = request.json
    query = """
        INSERT INTO Inmueble (Direccion, Ciudad, Estado, Codigo_Postal, Tipo_Inmueble, Precio_Venta, Descripcion)
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ID_inmueble;
    """
    values = (
        data["Direccion"],
        data["Ciudad"],
        data["Estado"],
        data["Codigo_Postal"],
        data["Tipo_Inmueble"],
        data["Precio_Venta"],
        data["Descripcion"],
    )

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    inmueble_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"ID_inmueble": inmueble_id}), 201


# Obtener todos los inmuebles
@app.route("/inmuebles", methods=["GET"])
def obtener_inmuebles():
    query = "SELECT * FROM Inmueble;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    inmuebles = cursor.fetchall()
    conn.close()

    return jsonify(inmuebles), 200


# Obtener un inmueble por ID
@app.route("/inmuebles/<int:inmueble_id>", methods=["GET"])
def obtener_inmueble(inmueble_id):
    query = "SELECT * FROM Inmueble WHERE ID_inmueble = %s;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (inmueble_id,))
    inmueble = cursor.fetchone()
    conn.close()

    return jsonify(inmueble), 200


# Registrar un cliente
@app.route("/clientes", methods=["POST"])
def registrar_cliente():
    data = request.json
    query = """
        INSERT INTO Cliente (Nombre, Apellido, Telefono, Email, Tipo_Cliente, Direccion)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING ID_cliente;
    """
    values = (
        data["Nombre"],
        data["Apellido"],
        data["Telefono"],
        data["Email"],
        data["Tipo_Cliente"],
        data.get("Direccion"),
    )

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    cliente_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"ID_cliente": cliente_id}), 201


# Obtener todos los clientes
@app.route("/clientes", methods=["GET"])
def obtener_clientes():
    query = "SELECT * FROM Cliente;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    clientes = cursor.fetchall()
    conn.close()

    return jsonify(clientes), 200


# Obtener un cliente por ID
@app.route("/clientes/<int:cliente_id>", methods=["GET"])
def obtener_cliente(cliente_id):
    query = "SELECT * FROM Cliente WHERE ID_cliente = %s;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (cliente_id,))
    cliente = cursor.fetchone()
    conn.close()

    return jsonify(cliente), 200


# Crear una transacción de compra/venta
@app.route("/transacciones", methods=["POST"])
def crear_transaccion():
    data = request.json
    query = """
        INSERT INTO Transaccion (Fecha_Transaccion, Tipo_Transaccion, Precio_Transaccion, Estado_Transaccion, 
                                 ID_inmueble, ID_cliente_comprador, ID_cliente_vendedor, ID_agente)
        VALUES (%s, %s, %s, 'En Proceso', %s, %s, %s, %s) RETURNING ID_transaccion;
    """
    values = (
        data["Fecha_Transaccion"],
        data["Tipo_Transaccion"],
        data["Precio_Transaccion"],
        data["ID_inmueble"],
        data.get("ID_cliente_comprador"),
        data.get("ID_cliente_vendedor"),
        data["ID_agente"],
    )

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    transaccion_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"ID_transaccion": transaccion_id}), 201


# Finalizar una transaccion
@app.route("/transacciones/<int:transaccion_id>", methods=["PUT"])
def finalizar_transaccion(transaccion_id):
    query = "UPDATE Transaccion SET Estado_Transaccion = 'Finalizado' WHERE ID_transaccion = %s"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, transaccion_id)
    transaccion_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(
        {"Se ha finalizado la transaccion con el ID_transaccion": transaccion_id}
    ), 201


# Obtener todas las transacciones
@app.route("/transacciones", methods=["GET"])
def obtener_transacciones():
    query = "SELECT * FROM Transaccion;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    transacciones = cursor.fetchall()
    conn.close()

    return jsonify(transacciones), 200


# Obtener una transacción por ID
@app.route("/transacciones/<int:transaccion_id>", methods=["GET"])
def obtener_transaccion(transaccion_id):
    query = "SELECT * FROM Transaccion WHERE ID_transaccion = %s;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (transaccion_id,))
    transaccion = cursor.fetchone()
    conn.close()

    return jsonify(transaccion), 200


# Registrar un pago
@app.route("/pagos", methods=["POST"])
def registrar_pago():
    data = request.json
    query = """
        INSERT INTO Pago (Fecha_Pago, Monto, Metodo_Pago, ID_transaccion)
        VALUES (%s, %s, %s, %s) RETURNING ID_pago;
    """
    values = (
        data["Fecha_Pago"],
        data["Monto"],
        data["Metodo_Pago"],
        data["ID_transaccion"],
    )

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    pago_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"ID_pago": pago_id}), 201


# Obtener todos los pagos
@app.route("/pagos", methods=["GET"])
def obtener_pagos():
    query = "SELECT * FROM Pago;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    pagos = cursor.fetchall()
    conn.close()

    return jsonify(pagos), 200


# Obtener un pago por ID
@app.route("/pagos/<int:pago_id>", methods=["GET"])
def obtener_pago(pago_id):
    query = "SELECT * FROM Pago WHERE ID_pago = %s;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (pago_id,))
    pago = cursor.fetchone()
    conn.close()

    return jsonify(pago), 200


# Eliminar un pago por ID
@app.route("/pagos/<int:pago_id>", methods=["DELETE"])
def eliminar_pago(pago_id):
    query = "DELETE FROM Pago WHERE ID_pago = %s RETURNING ID_pago;"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (pago_id,))
    eliminado_id = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    if eliminado_id:
        return jsonify({"ID_pago_eliminado": eliminado_id[0]}), 200
    else:
        return jsonify({"error": "Pago no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
