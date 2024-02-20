from cloudlink import cloudlink

if __name__ == "__main__":
    cl = cloudlink()

    server = cl.server(logs=True)

    # Set the message-of-the-day.
    server.set_motd("Welcome to Themadpunter's CloudChat server. Some channels include #help, #anonchat, #main, #nork (for norking), #codesource, and #nerk.", True)
    # Run the server.
    server.run(ip="0.0.0.0", port=3000)
