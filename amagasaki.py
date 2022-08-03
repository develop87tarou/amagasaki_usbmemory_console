print ("==========================")
print ("尼崎市　USBメモリーコンソール")
print ("helpコマンドを使用してヘルプを表示")
print ("==========================")
breaker = "on"
door = "on"
power = "on"
battery = 100
reboot = 0
while True:
	print ("===============================")
	battery2  = str(battery)
	if breaker == "off":
		door = "off"
		print("ドアロック解除")
		print("現在ブレーカーが停止しています。電源操作以外の機能が停止しています。")
		print("system rebootを使用し再起動するか、電力供給を止め強制的にシステムを終了させてください。")
	if power == "off" and battery <= 0:
		print("電力なし")	
		break
	if power ==  "off" and breaker == "on":
		battery -= 10
		print("現在予備電力で作動しています。残量")
		print(battery)
	elif power == "on":
		battery += 3
	if battery >= 100:
		battery = 100
	a = input(">")
	if a == "access main memory":
		if breaker == "on":
				page = int(input("ページ(1~46000)>"))
				if page <= 0:
					print("数値エラー。1~46000の数値を入力")
				elif page < 46000:
					pas = str(input("パスワード>"))
					if pas == "amagasaki2022":
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						print ("田中＿太郎0*0-0000-0000-〒000-0000")
						page2 = str(page)
						print ("page-"+page2+"/46000")
					else:
						print ("アクセス拒否")
				else:
					print ("数値エラー。1~46000の数値を入力")
		else:
			print("使用するにはブレーカーを再起動してください")
	elif a == "access main security":
		pas = input("パスワード>")
		if pas == "amagasaki2022":
			print ("ブレーカー-1 ドアロック-2  + on/off")
			sec = input(">")
			if sec == "1 on":
				print("ブレーカーオン")
				breaker = "on"
			elif sec == "1 off":
				print("ブレーカーオフ")
				breaker = "off"
			elif sec == "2 on":
				print("ドアロックオン")
				door = "on"
			elif sec == "2 off":
				print("ドアロックオフ")
				door = "off"
		else:
			print("アクセス拒否")
	elif a == "exit":
		break
	elif a == "help":
		print("comamnd1===access===")
		print("機能にアクセスします。")
		print("main memory")
		print("main security")
		print("sub systems")
		print("command2===exit===")
		print("comamnd3===amagasakistats===")
		print("尼崎市役所の状態を確認できます。")
		print("command4===system reboot===")
		print("=====================")
		print("パスワード:amagasaki2022")
	elif a == "amagasakistats":
		if breaker == "on":
			if  breaker == "on":
				print("ブレーカーオン")
			else:
				print("ブレーカーオフ")
			if door == "on":
				print("ドアロックオン")
			else:
				print("ドアロックオフ")
			if power == "on":
				print("電力が供給されています")
			else:
				print("電力が供給されていません")
				print("予備電力残量")
				print(battery)
		else:
			print("使用するにはブレーカーを再起動してください")
	elif a == "access":
		print ("access (対象)")
		print ("詳細はhelpコマンドを使用してください")
	elif a == "access sub systems":
		if breaker == "on":
			print("外部電力供給-1-off/on 予備電源残量-2")
			sub = input("サブシステム>")
			if sub == "1 off":
				print("電力供給オフ")
				power = "off"
			elif sub == "1 on":
				print("電力供給オン")
				power = "on"
			elif sub == "2":
				print("予備電力残量")
				print(battery)
			else:
				print("エラー")
		elif breaker == "off":
			print("使用するにはブレーカーを再起動してください")
	elif a == "system reboot":
		while reboot < 30:
			print()
			reboot += 1
		reboot = 0
		breaker = "on"
		door = "on"
		power = "on"
		print ("==========================")
		print ("尼崎市　USBメモリーコンソール")
		print ("helpコマンドを使用してヘルプを表示")
		print ("==========================")
	else:
		print("エラー")
