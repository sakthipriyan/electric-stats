# Electric Stats
Electricity status aggregator from Raspberry Pi.

## REST API

### Sync status
Only API endpoint which has to be called by the bots.

#### Request
    POST /sync
    Host: http://electric-stats.appspot.com/
    Authorization: KEY <SECRET_KEY>
    {
    	"events": [
    		{"timestamp":1436416231,"status":0}
    	]
    }

#### Success Response
When uploaded data is successfully saved.

    201 Created

#### Error Responses
In case, if the Authorization header is invalid.

    401 Unathorized

In case, if the input json is invalid.

    400 Bad Request
