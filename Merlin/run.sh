if [ -z "$1" ]; then
    echo 'You must provide a port'
    exit 1
fi
tmux new -d -s 'deerhunt'
tmux send-keys "python runServer.py --render $1" C-m
tmux new-window
tmux send-keys "sleep 3 && python runClient.py $(hostname) $1" C-m
tmux split -h
tmux send-keys "sleep 1 && python runClient.py $(hostname) $1" C-m
tmux next-window
