import requests


def trigger_daily_roue(php_session_id: str) -> tuple[int, str]:
    """
    trigger_daily_roue: Effectue une requete sur le site minestrator.com automatiquement.
    (en se consentrant sur la roue de la fortune quotidienne)

    Args:
        php_session_id (str): PHPSESSID

    Returns:
        tuple[int, str]: Retourne le code de statut de la requete et le contenu de la reponse.

    """


    url = "https://minestrator.com/action.php?action=daily_roue_fortune"

    headers = {
        "authority": "minestrator.com",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "dnt": "1",
        "origin": "https://minestrator.com",
        "referer": "https://minestrator.com/roue/de/la/fortune",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    cookies = {
        "cf_checks": "aqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmQUFR",
        "language": "fr",
        "_ga": "GA1.1.623905678.1741614692",
        "_gcl_au": "1.1.1965685299.1741614692",
        "_tt_enable_cookie": "1",
        "_ttp": "01JP056EBKKT1NPSCT5T8P6K37_.tt.1",
        "PHPSESSID": php_session_id,
        "_ga_JEXEM1KE28": "GS1.1.1742396056.4.1.1742396064.0.0.0"
    }

    response = requests.post(url, headers=headers, cookies=cookies)
    return response.status_code, response.text


def get_delay_before_next_wheel(php_session_id: str) -> int:
    """
    get_delay_before_next_wheel: Récupère le temps restant avant de pouvoir faire tourner la roue de la fortune.

    Args:
        php_session_id (str): PHPSESSID

    Returns:
        int: Retourne le temps restant en secondes.
    """

    url = "https://minestrator.com/action.php?action=get_daily_drop_info"

    headers = {
        "authority": "minestrator.com",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "dnt": "1",
        "origin": "https://minestrator.com",
        "referer": "https://minestrator.com/roue/de/la/fortune",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    cookies = {
        "cf_checks": "aqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmaqSmQUFR",
        "language": "fr",
        "_ga": "GA1.1.623905678.1741614692",
        "_gcl_au": "1.1.1965685299.1741614692",
        "_tt_enable_cookie": "1",
        "_ttp": "01JP056EBKKT1NPSCT5T8P6K37_.tt.1",
        "PHPSESSID": php_session_id,
        "_ga_JEXEM1KE28": "GS1.1.1742396056.4.1.1742396064.0.0.0"
    }

    response = requests.post(url, headers=headers, cookies=cookies)
    return response.status_code, response.text

    