import sqlite3

# Conectar ao banco de dados SQLite (ele será criado se não existir)
conn = sqlite3.connect('posto_saude_bom_jesus.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    funcionario_id INTEGER NOT NULL,
    data_consulta DATE NOT NULL,
    hora_consulta TIME NOT NULL,
    descricao TEXT,
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id),
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id)
)
''')

# Inserir dados de exemplo na tabela de Pacientes
cursor.executemany('''
INSERT INTO Pacientes (nome, data_nascimento, endereco, telefone, email)
VALUES (?, ?, ?, ?, ?)
''', [
    ('João Silva', '1985-03-15', 'Rua A, 123', '99999-1111', 'joao@example.com'),
    ('Maria Oliveira', '1990-07-22', 'Rua B, 456', '99999-2222', 'maria@example.com')
])

# Inserir dados de exemplo na tabela de Funcionarios
cursor.executemany('''
INSERT INTO Funcionarios (nome, cargo, telefone, email)
VALUES (?, ?, ?, ?)
''', [
    ('Dr. Carlos Mendes', 'Médico', '99999-3333', 'carlos@example.com'),
    ('Enf. Ana Souza', 'Enfermeira', '99999-4444', 'ana@example.com')
])

# Inserir dados de exemplo na tabela de Consultas
cursor.executemany('''
INSERT INTO Consultas (paciente_id, funcionario_id, data_consulta, hora_consulta, descricao)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, 1, '2024-08-10', '09:00', 'Consulta de rotina'),
    (2, 2, '2024-08-11', '10:00', 'Consulta de acompanhamento')
])

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
