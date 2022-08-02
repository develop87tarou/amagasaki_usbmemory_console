print ("==========================")
print ("尼崎市　USBメモリーコンソール")
print ("helpコマンドを使用してヘルプを表示")
print ("==========================")
breaker = "on"
door = "on"
while True:
	print ("===============================")
	a = input(">")
	if a == "access main memory":
			page = int(input("ページ(1~46000)>"))
			if page <= 0 and page >=46001:
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
				print("数値エラー。1~46000の数値を入力")
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
		print("command2===exit===")
		print("comamnd3===amagasakistats===")
		print("尼崎市役所の状態を確認できます。")
	
	elif a == "amagasakistats":
		if  breaker == "on":
			print("ブレーカーオン")
		else:
			print("ブレーカーオフ")
		if door == "on":
			print("ドアロックオン")
		else:
			print("ドアロックオフ")
	elif a == "access":
		print ("access (対象)")
		print ("詳細はhelpコマンドを使用してください")
	else:
		print("エラー")
