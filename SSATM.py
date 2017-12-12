from flask import Flask,request,redirect,url_for,session,render_template

app=Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=["GET","POST"])
def atmside():
	try:
		balance=session["balance"]
		count=session["count"]
	except KeyError:
		balance=session["balance"]=0;
		count=session["count"]=0;	

	if(request.method=="GET"):
		return render_template("atm.html",balance=balance,count=count)

	if(request.method=="POST"):
		if(count==5):
			msg="Completed 5 Transactions!"
			session.clear()
			return render_template("atm.html",balance=balance,msg=msg,count=count)
		if(request.form["action"]=="Withdraw"):
			if(int(request.form["amount"])>5000):
				msg="Cannot Withdraw more than Rs.5000/-"
				return render_template("atm.html",balance=balance,count=count,msg=msg)
			elif(int(request.form["amount"])>balance):
				msg="Cannot Withdraw more than Balance!"
				return render_template("atm.html",balance=balance,count=count,msg=msg)
			else:
				balance=balance-int(request.form["amount"])
				count=count+1
				session["balance"]=balance
				session["count"]=count
				msg="Amount Withdrawn"
				return render_template("atm.html",balance=balance,count=count,msg=msg)

		elif(request.form["action"]=="Deposit"):
			if(int(request.form["amount"])>10000):
				msg="Cannot Deposit more than Rs.10000/-"
				return render_template("atm.html",msg=msg)
			else:
				balance=balance+int(request.form["amount"])
				count=count+1
				session["balance"]=balance
				session["count"]=count
				msg="Amount Deposited"
				return render_template("atm.html",balance=balance,count=count,msg=msg)
				

if(__name__=='__main__'):
	app.run()
		
