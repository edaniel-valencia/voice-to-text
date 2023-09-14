<!DOCTYPE html>
<html>
<head>
    <title>Transcripción de Audio</title>
</head>
<body>
    <h1>Transcripción de Audio</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="audio" accept=".wav">
        <button type="submit">Transcribir</button>
    </form>
    {% if transcription %}
    <h2>Texto Transcrito:</h2>
    <p>{{ transcription }}</p>
    {% endif %}
</body>
</html>
