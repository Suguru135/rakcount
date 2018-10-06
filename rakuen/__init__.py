


def authenticate(driver, id_str, pass_str):
    """ログイン認証関数
    driver : seleniumのwebdriverインスタンス
    id_str : ログインID (String)
    pass_str : ログインPASSWORD (String)
    
    成功すればTrue, 失敗すればFalseを返します
    """
    #ログイン
    driver.get('http://rakuen.jeison.biz/bbs/user/login.php?mode=thread')
    
    r_id = driver.find_element_by_name('id')
    r_id.send_keys(id_str)
    r_pass = driver.find_element_by_name('pass')
    r_pass.send_keys(pass_str)
    driver.find_element_by_name('submit').click()

    if driver.title == 'ユーザーページ':
        return True

    else:
        return False


def post(driver, no, name, mail, contents, filepath=None):
    """レス投稿関数
    driver : seleniumのwebdriverインスタンス
    no : スレッド番号 (String)
    name : ハンドルネーム (String)
    mail : メールアドレス (String)
    contents : 書き込み内容 (String)
    filepath : 画像ファイルの絶対パス (String) (任意)
    
    成功すればTrue、失敗すればログを出力してFalseを返します
    """

    driver.get('http://rakuen.jeison.biz/bbs/read.php?mode=thread&no=' + no + '&res=n1')
    r_name = driver.find_element_by_name('name')
    r_name.clear()
    r_name.send_keys(name)
    
    r_mail = driver.find_element_by_name('mail')
    r_mail.clear()
    r_mail.send_keys(mail)

    r_contents = driver.find_element_by_name('contents')
    r_contents.clear()
    r_contents.send_keys(contents)

    if filepath != None:
        r_filepath = driver.find_element_by_name('file')
        r_filepath.clear()
        r_filepath.send_keys(filepath)


    driver.find_element_by_name('submit').click()

    if driver.title != 'えらー':
        return True

    else:
        print(driver.page_source)
        return False
