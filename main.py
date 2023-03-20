from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.horariodebrasilia.org/")
date = driver.find_element('xpath','//*[@id="dia-topo"]').text
driver.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cota%C3%A7%C3%A3o+dolar&aqs=chrome.0.69i59j0i433i512l2j0i131i433i512j0i512l5j0i433i512.1396j0j4&sourceid=chrome&ie=UTF-8')
dolar_value = driver.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
driver.get('https://letterboxd.com/victor78992/')
following_letterboxd = driver.find_element('xpath', '//*[@id="profile-header"]/div/div[4]/div[1]/h4[4]/a/span[1]').text
followers_letterboxd = driver.find_element('xpath', '//*[@id="profile-header"]/div/div[4]/div[1]/h4[5]/a/span[1]').text
print("A Data de hoje é {}".format(date))
print("A cotação atual do dolar é {}".format(dolar_value))
print("Minha quantidade de seguidores no letterboxd é {}".format(followers_letterboxd))
print("A quantidade de pessoas que sigo no letterboxd é {}".format(following_letterboxd))