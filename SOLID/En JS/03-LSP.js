function makeRequest(url, errorHandler) {
    fetch(url)
        .then(response => response.json())
        .catch(error => {
            errorHandler.handle(error);
        });
}

const consoleErrorHandler = {
    handle: function(error) {
        console.error(error);
    }
};

const externalErrorHandler = {
    handle: function(error) {
        sendErrorToExternalService(error);
    }
};

// Usos de makeRequest
makeRequest('https://my-api.com/data', consoleErrorHandler);
makeRequest('https://my-api.com/data', externalErrorHandler);
