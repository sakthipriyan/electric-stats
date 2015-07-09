# Electric Stats

Simple mechanism to collect and analyze availability of electricity.
Electric Stats contains two parts
* [py-client](py-client/README.md) - which runs on Raspberry Pi to collect electricity availability.
* [go-server](go-server/README.md) - which runs on Google App Engine which can receive data from these py-client over http.
