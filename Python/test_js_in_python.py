import execjs

# Lire le contenu du fichier JavaScript
with open('aliexpressProductScraper.js', 'r') as f:
    js_code = f.read()

# Compiler le code JavaScript
js = execjs.compile(js_code)

# Exécuter une fonction JavaScript
result = js.call('AliexpressProductScraper', '1005004840696277')

# Afficher le résultat
print(result)