import redis
 
 
# The operation to perform for each event
def add_new_win(conn, winner):
    conn.zincrby('wins_counter', 1, winner)
    conn.incr('total_games_played')
 
def main():
    # Connect to Redis
    conn = redis.Redis()
    # Tail the event stream
    last_id = '$'
    while True:
        events = conn.xread({'wins_stream': last_id}, block=0, count=10)
        # Process each event by calling `add_new_win`
        for _, e in events:
            winner = e['winner']
            add_new_win(conn, winner)
            last_id = e['id']
 
if __name__ == '__main__':
    main()