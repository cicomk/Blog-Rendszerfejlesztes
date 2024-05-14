-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2024. Máj 01. 23:58
-- Kiszolgáló verziója: 10.4.27-MariaDB
-- PHP verzió: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `beadando`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `body` varchar(300) NOT NULL,
  `timestamp` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `comments`
--

INSERT INTO `comments` (`id`, `user_id`, `topic_id`, `body`, `timestamp`) VALUES
(1, 1, 1, 'Nagyon jó', '2024-03-29 12:20:07'),
(2, 1, 2, 'Megesik', '2024-02-18 12:20:07'),
(3, 2, 2, 'asd', '2024-03-21 12:20:07'),
(4, 3, 2, 'asdasdasdas', '2024-04-16 23:44:50.067776'),
(5, 3, 1, 'asdadsdasd', '2024-04-16 23:54:31.195910'),
(6, 3, 3, 'Szervuuusz', '2024-04-17 00:14:33.454661'),
(7, 3, 1, 'dsd', '2024-04-17 22:23:52.944070'),
(8, 3, 3, 'dsdsds', '2024-04-17 22:24:01.380339'),
(9, 3, 3, 'Szia', '2024-04-30 22:02:27.407738'),
(10, 3, 3, 'adasdasdas', '2024-04-30 22:02:42.038820'),
(11, 1, 3, 'asd', ''),
(12, 3, 2, '123123', '2024-05-01 20:54:45.944899'),
(13, 1, 1, '123', '2024-05-01 21:05:04.450322'),
(14, 4, 2, 'asdasdasdas', '2024-05-01 21:07:42.509345'),
(15, 4, 4, 'Szia Bajusz', '2024-05-01 21:08:17.015871');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `topics`
--

CREATE TABLE `topics` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type_id` int(10) NOT NULL,
  `description` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `topics`
--

INSERT INTO `topics` (`id`, `name`, `type_id`, `description`) VALUES
(1, 'asd', 1, 'jkl'),
(2, '23424234', 1, '23423423'),
(3, 'asd', 2, 'dfs'),
(4, 'a3', 2, 'fd'),
(5, 'Próba', 1, 'asd');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `topic_types`
--

CREATE TABLE `topic_types` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `topic_types`
--

INSERT INTO `topic_types` (`id`, `name`) VALUES
(1, 'Utazás'),
(2, 'Étel');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `admin` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `users`
--

INSERT INTO `users` (`id`, `username`, `name`, `password`, `admin`) VALUES
(1, 'randuser', 'RandomUser', '1234', 0),
(2, 'EricCartman', 'Eric Cartman', '1234', 0),
(3, 'LocalUser', 'LocalUser', '1234', 0),
(4, 'admin', 'Koppány', '1234', 1);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `topics`
--
ALTER TABLE `topics`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `topic_types`
--
ALTER TABLE `topic_types`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT a táblához `topics`
--
ALTER TABLE `topics`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT a táblához `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
