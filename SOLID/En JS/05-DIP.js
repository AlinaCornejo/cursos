class MySQLConnection{
    connect(){

    }
}

class PasswordReminder{
    constructor(dbConnection) {
        this.dbConnection = new MySQLConnection();
    }
}