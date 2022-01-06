## General Testing Guide
Below is a general guide of how different kinds of testing work. Before continuing, please **ensure to have the associated [setup completed](https://github.com/UTM-Robotics/Deerhunt-Battlecode2021#readme)**.

The flag server which is run via `python3 ./runServer.py localhost <port> [--verbose] [--render]` where the verbose flag enables the printing of the map in json form, and the render flag renders the game using pygame.
The verbose flag also ensures that once clients have computed you must press enter in the terminal to see the next tick be computed.

Note, there is a timeout on the server. If you do not connect your clients within the set 10s from eachother, you will have to restart the server.

### Local Testing - Automated
**Note: Requires use of bash. If not comfortable, it may be best to follow manual testing##
   Enclosed is a `run.sh` file. This script automatically will run the server
   as well as both of the clients inside `tmux` (you need `tmux` installed for
   the script to work). You can run the script by typing `./run.sh 8888`. You 
   may need to change the port number if you're running the script frequently.

   The script will open `tmux` launch the server, then make a new tab and launch
   your client twice. You can navigate between the tabs by pressing =C-b n= (control b then n).

### Local Testing - Manual
   Alternatively you can launch the server and two clients manually in 3 seprate terminals.
   To do so, you will use `Merlin/runServer.py` (Mac has a seperate server) and `Merlin/runClient.py`
   from within repository root.
   For tips on how to navigate directories with your bash (wsl or MacOS) terminal, you may find https://help.ubuntu.com/community/UsingTheTerminal to be of use.
#### General Manual Steps
1. Open 3 terminals (Windows users ensure use Ubuntu installed WSL)

2. Go to project "Merlin" folder.
   `cd Merlin` from project root
3. Run Server on terminal 1(within root)
   `python3  ./runServer.py 8888` where server is "server" and "mac_os_server". To enable rendering, please use
   `python3  ./runServer.py 8888 --render` instead.

4. Run Player 1 terminal 2(From Merlin folder)
   `python3  ./runClient.py localhost 8888 

5. Run Player2 terminal 3(From Merlin folder)
   `python3  ./runClient.py localhost 8888`



#### Note:
 To run a different ai client, swap `./runClient.py` with  `./runClient2.py`. This allows you to run the client in `Merlin/client2` instead.
