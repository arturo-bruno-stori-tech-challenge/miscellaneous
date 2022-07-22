-- clients_transactions.clients definition

CREATE TABLE `clients` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(30) NOT NULL,
    `email` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`id`)
)
