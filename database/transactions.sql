-- clients_transactions.transactions definition

CREATE TABLE `transactions` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `client_id` int unsigned NOT NULL,
    `transaction_id` int NOT NULL,
    `date` date NOT NULL,
    `amount` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `client_transactions` (`client_id`,`transaction_id`),
    CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE CASCADE
)
