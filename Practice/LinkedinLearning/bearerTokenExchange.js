const accessTokenExchange = async() => {
    const response = await fetch(
        "https://api.us.flatfile.io/auth/access-key/exchange", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                accessKeyId: 'FF00UL3BZLO43DPTUYUAJ8GB2QK6Q82N54QV30EW',
                secretAccessKey: 'PJ0t0F32PgvcyGjl7JjW0wqSUcrYpfRWvuRJszKb',
                expiresIn: 86400 // default: 43200 (12 hours) minimum: 60 (1 minute) maximum: 86400 (24 hours)
            })
        }
    );
    return response.json();
}