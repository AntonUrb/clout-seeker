import requests
import bs4
import undetected_chromedriver as uc


def check(username):
    """
    We are going to check whether username exists on:

    :param username:
    :return:
    """
    username = username.replace("@", "")
    platforms = ["Pinterest", "Tumblr", "Twitter", "Github", "Reddit"]
    checks = {}
    final_str = ""
    for platform in platforms:
        checks[platform] = check_username(platform, username)
        final_str += f"{platform} : {'no' if checks[platform] else 'yes'}\n"
    print(checks)
    return final_str


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Referer": "https://checkusernames.com",
    "X-Requested-With": "XMLHttpRequest"
}


def check_username(platform, username):
    if platform == "Twitter":
        return twitter(username)
    if platform == "Reddit":
        return reddit(username)
    response = requests.get(
        f"https://checkusernames.com/usercheckv2.php?target={platform}&username={username}&time=1708771782484",
        headers=headers)
    return "Not Available" not in response.text


def reddit(username):
    result = requests.get(f"https://www.reddit.com/user/" + username)
    if result.status_code == 200:
        if "Sorry, nobody on Reddit goes by that name." in result.text:
            return True
    return False


def twitter(username):
    driver = uc.Chrome(headless=True, use_subprocess=False)
    driver.get("https://twitter.com/" + username)
    if "This account doesn’t exist" in driver.page_source:
        driver.close()
        driver.quit()
        return True
    driver.close()
    driver.quit()
    return False
