if [ -z "$1" ]; then
    echo 'You must provide a port'
    exit 1
fi
tmux new -d -s 'deerhunt'
tmux send-keys "Merlin/runServer.py --render --verbose $1" C-m
tmux new-window
tmux send-keys "sleep 3 && Merlin/client/runClient.py $(hostname) $1" C-m
tmux split -h
tmux send-keys "sleep 1 && Merlin/client/runClient.py $(hostname) $1" C-m
tmux next-window

tmux a