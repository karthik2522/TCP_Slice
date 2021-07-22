# TCP_Slice
   
     Write a TCP splice connect program. Essentially, two clients connects to it and whatever client 1 sends to it, 
     it forwards the same to client 2 and vice versa.The program is to be invoked as ./program -p <port number>

     Open Terminal or Press ctrl+Alt+T

     gedit tcp_client.py and save it

     gedit tcp_server.py and save it

# Run Program 

    open terminal and type the command as python tcp_server.py <IP Address> <Port Number>


    Example: python tcp_server.py 127.0.0.1 8080

    Open another terminal and type the command as python tcp_client.py <IP Address> <Port number>

    Example: python tcp_client.py 127.0.0.1 8080
