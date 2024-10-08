PRAGMA encoding = "UTF-8";

CREATE TABLE IF NOT EXISTS artistas (
  id integer PRIMARY KEY autoincrement,
  nome varchar(45) NOT NULL,
  gravadoras_id integer NOT NULL,
  created timestamp NULL DEFAULT NULL,
  modified timestamp NULL DEFAULT NULL
);

INSERT INTO artistas (id, nome, gravadoras_id, created, modified) VALUES
(1, 'Mano Lima', 2, '2019-10-18 16:28:53', '2019-10-18 16:28:53'),
(2, 'Shakira', 4, '2019-10-18 16:29:46', '2019-10-18 16:29:46'),
(3, 'Luiz Marenco', 5, '2019-10-18 16:30:29', '2019-10-18 16:30:29'),
(4, 'Pedro Capó', 4, '2019-10-21 20:15:53', '2019-10-21 20:15:53'),
(5, 'Farruko', 4, '2019-10-21 20:16:19', '2019-10-21 20:16:19'),
(6, 'Alicia Keys', 4, '2019-10-21 20:16:28', '2019-10-21 20:16:28'),
(7, 'Joca Martins', 2, '2019-10-21 20:18:46', '2019-10-21 20:18:46'),
(8, 'José Cláudio Machado', 2, '2019-10-21 20:19:24', '2019-10-21 20:19:24'),
(9, 'Luis Fonsi', 4, '2019-10-21 20:23:42', '2019-10-21 20:23:42'),
(10, 'Nicky Jam', 4, '2019-10-21 20:25:48', '2019-10-21 20:25:48'),
(11, 'Enrique Iglesias', 4, '2019-10-21 20:45:55', '2019-10-21 20:45:55'),
(12, 'Gente de Zona', 4, '2019-10-21 20:46:07', '2019-10-21 20:46:07'),
(13, 'Descemer Bueno', 4, '2019-10-21 20:46:24', '2019-10-21 20:46:24'),
(14, 'Zion', 4, '2019-10-21 21:00:07', '2019-10-21 21:00:07'),
(15, 'Lennox', 4, '2019-10-21 21:00:16', '2019-10-21 21:00:16'),
(16, 'Maluma', 4, '2019-10-21 21:01:32', '2019-10-21 21:01:32'),
(17, 'Anitta', 4, '2019-10-21 21:01:43', '2019-10-21 21:01:43'),
(18, 'Mettallica', 4, '2019-10-21 21:02:34', '2019-10-21 21:02:34'),
(19, 'MC Créu', 1, '2019-10-21 21:22:44', '2019-10-21 21:22:44');

CREATE TABLE IF NOT EXISTS clientes (
  id integer PRIMARY KEY autoincrement,
  login varchar(45) NOT NULL,
  senha varchar(45) NOT NULL,
  created timestamp NULL DEFAULT NULL,
  modified timestamp NULL DEFAULT NULL,
  planos_id integer NOT NULL,
  email varchar(50) DEFAULT NULL
);

INSERT INTO clientes (id, login, senha, created, modified, planos_id, email) VALUES
(1, 'Sandro', '5andr0', '2019-10-18 16:08:20', '2019-10-21 20:52:17', 1, 'sandrocamargo@unipampa.edu.br'),
(2, 'Papa', 'v5t1c5n0', '2019-10-18 16:08:51', '2019-10-21 20:52:42', 3, 'papa@vaticano.com'),
(3, 'Neymar', 'caicai', '2019-10-21 20:14:56', '2019-10-21 20:53:08', 3, 'bateu-caiu@selecao.com');

CREATE TABLE IF NOT EXISTS generos (
  id integer PRIMARY KEY  autoincrement,
  descricao varchar(45) NOT NULL,
  created timestamp NULL DEFAULT NULL,
  modified timestamp NULL DEFAULT NULL
);

INSERT INTO generos (id, descricao, created, modified) VALUES
(1, 'Gaúcha', '2019-10-18 16:10:38', '2019-10-18 16:10:38'),
(2, 'Pop', '2019-10-18 16:10:42', '2019-10-18 16:10:42'),
(3, 'Rock', '2019-10-18 16:10:46', '2019-10-18 16:10:46'),
(4, 'Funk', '2019-10-18 16:10:49', '2019-10-18 16:10:49');

CREATE TABLE IF NOT EXISTS gravadoras (
  id integer primary key autoincrement,
  nome varchar(45) NOT NULL,
  valor_contrato decimal(10,0) NOT NULL,
  vencimento_contrato date DEFAULT NULL,
  created timestamp NULL DEFAULT NULL,
  modified timestamp NULL DEFAULT NULL
);

INSERT INTO gravadoras (id, nome, valor_contrato, vencimento_contrato, created, modified) VALUES
(1, 'Artista Independente', 0, '2020-12-31', '2019-10-18 16:18:32', '2019-10-18 16:18:32'),
(2, 'ACIT', 50000, '2020-12-31', '2019-10-18 16:28:19', '2019-10-18 16:28:19'),
(3, 'Som Livre', 100000, '2020-12-31', '2019-10-18 16:28:38', '2019-10-18 16:28:38'),
(4, 'Sony Music', 500000, '2024-12-31', '2019-10-18 16:29:37', '2019-10-18 16:29:37'),
(5, 'USA Discos', 10000, '2020-12-31', '2019-10-18 16:30:21', '2019-10-18 16:30:21');

CREATE TABLE IF NOT EXISTS musicas (
  id integer PRIMARY KEY  autoincrement,
  nome varchar(45) NOT NULL,
  duracao time NOT NULL,
  generos_id integer NOT NULL,
  lancamento date DEFAULT NULL,
  created timestamp NULL DEFAULT NULL,
  modified timestamp NULL DEFAULT NULL
);

INSERT INTO musicas (id, nome, duracao, generos_id, lancamento, created, modified) VALUES
(1, 'Conta pro tio', '04:00:00', 1, '2014-01-01', '2019-10-18 16:31:22', '2019-10-18 16:31:22'),
(2, 'Balaio de gato', '03:05:00', 1, '2014-10-07', '2019-10-21 15:06:51', '2019-10-21 15:06:51'),
(3, 'Batendo água', '15:09:00', 1, '2014-02-06', '2019-10-21 15:09:57', '2019-10-21 15:09:57'),
(4, 'Estoy aqui', '05:00:00', 2, '2014-04-05', '2019-10-21 15:18:10', '2019-10-21 15:18:10'),
(5, 'Calma', '20:15:00', 2, '2018-12-31', '2019-10-21 20:15:36', '2019-10-21 20:15:36'),
(6, 'A boa vista do peão de tropa', '04:18:00', 1, '2014-12-31', '2019-10-21 20:18:37', '2019-10-21 20:18:37'),
(7, 'Espantando o Bagual', '04:00:00', 1, '2014-12-31', '2019-10-21 20:21:20', '2019-10-21 20:21:20'),
(8, 'Cadela Baia', '03:59:00', 1, '2014-12-31', '2019-10-21 20:22:05', '2019-10-21 20:22:05'),
(9, 'Sem paia e sem fumo', '03:59:00', 1, '2014-12-31', '2019-10-21 20:22:52', '2019-10-21 20:22:52'),
(10, 'Despacito', '04:00:00', 2, '2014-12-31', '2019-10-21 20:23:30', '2019-10-21 20:23:30'),
(11, 'Quando o verso vem pras casa', '04:00:00', 1, '2014-12-31', '2019-10-21 20:24:28', '2019-10-21 20:24:28'),
(12, 'Perro Fiel', '03:59:00', 2, '2014-12-31', '2019-10-21 20:26:15', '2019-10-21 20:26:15'),
(13, 'Bailando', '04:00:00', 2, '2014-12-31', '2019-10-21 20:46:59', '2019-10-21 20:46:59'),
(14, 'El perdón', '03:54:00', 2, '2014-12-31', '2019-10-21 20:54:37', '2019-10-21 20:54:37'),
(15, 'Súbeme la Radio', '03:30:00', 2, '2014-12-31', '2019-10-21 21:00:39', '2019-10-21 21:00:39'),
(16, 'Sim ou Não', '04:00:00', 2, '2014-12-31', '2019-10-21 21:00:48', '2019-10-21 21:02:16'),
(17, 'Felices los 4', '03:59:00', 2, '2014-12-31', '2019-10-21 21:21:54', '2019-10-21 21:21:54'),
(18, 'Dança do Créu', '01:59:00', 4, '2014-12-31', '2019-10-21 21:22:59', '2019-10-21 21:22:59');

CREATE TABLE IF NOT EXISTS musicas_has_artistas (
  id intEGER PRIMARY KEY  autoincrement,
  musicas_id integer NOT NULL,
  artistas_id integer NOT NULL
);

INSERT INTO musicas_has_artistas (id, musicas_id, artistas_id) VALUES
(00000000001, 1, 1),
(00000000002, 2, 1),
(00000000003, 3, 3),
(00000000004, 4, 2),
(00000000005, 5, 4),
(00000000006, 5, 5),
(00000000007, 5, 6),
(00000000008, 6, 8),
(00000000009, 6, 7),
(00000000010, 6, 3),
(00000000011, 7, 1),
(00000000012, 8, 1),
(00000000013, 9, 1),
(00000000014, 10, 9),
(00000000015, 11, 3),
(00000000016, 12, 2),
(00000000017, 12, 10),
(00000000018, 13, 13),
(00000000019, 13, 11),
(00000000020, 13, 12),
(00000000021, 14, 11),
(00000000022, 14, 10),
(00000000023, 16, 17),
(00000000024, 16, 16),
(00000000025, 15, 11),
(00000000026, 15, 15),
(00000000027, 15, 14),
(00000000028, 15, 13),
(00000000029, 17, 16),
(00000000030, 18, 19);

CREATE TABLE IF NOT EXISTS musicas_has_clientes (
  id integer PRIMARY KEY  autoincrement,
  musicas_id integer NOT NULL,
  clientes_id integer NOT NULL,
  data timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO musicas_has_clientes (id, musicas_id, clientes_id, data) VALUES
(00000000001, 4, 1, '2019-10-21 15:19:00'),
(00000000002, 1, 1, '2019-10-21 21:28:00'),
(00000000003, 1, 1, '2019-10-21 21:29:00');

CREATE TABLE IF NOT EXISTS pagamentos (
  id integer PRIMARY KEY  autoincrement,
  data date DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS planos (
  id integer PRIMARY KEY autoincrement,
  descricao varchar(45) NOT NULL,
  valor decimal(5,2) NOT NULL,
  limite integer NOT NULL,
  created timestamp NULL DEFAULT NULL,
  modified timestamp NULL DEFAULT NULL
);

INSERT INTO planos (id, descricao, valor, limite, created, modified) VALUES
(1, 'Light', 29.99, 100, '2019-10-18 14:21:08', '2019-10-18 14:21:08'),
(2, 'Sem nome', 39.99, 500, '2019-10-18 14:21:31', '2019-10-18 14:21:31'),
(3, 'Full', 49.99, 999999, '2019-10-18 14:22:00', '2019-10-18 14:22:00');