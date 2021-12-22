from flask import Flask,render_template,request,redirect,url_for,flash, jsonify, session
import json
import pymysql
import pandas as pd

# Create Flask instance
app = Flask(__name__)
# Add our database
conn = pymysql.connect(host = 'final-project-fe595-group7.cz2xzj6pvabe.us-east-2.rds.amazonaws.com',
                      port = 3306,
                      user = 'admin',
                      password = 'group72021',
                      db = 'FinalprojectFE595Group7')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:group72021@final-project-fe595-group7.cz2xzj6pvabe.us-east-2.rds.amazonaws.com/FinalprojectFE595Group7'

app.secret_key = 'workgroup595'
@app.route('/')

def home():

    return render_template('home.html')

@app.route('/search', methods = ['GET','POST'])

def search():

    if request.method == 'POST':


        Info = {}

        Info['source'] = request.form.get("source")
        Info['Subject'] = request.form['subject']
        Info['start_date'] = request.form['startdate']
        Info['end_date'] = request.form['enddate']


        with open('Info.json', 'w') as Data_file:
            json.dump(Info, Data_file)


        f = open('Info.json')
        info = json.load(f)

        text = info['Subject']
        sdate = info['start_date']
        edate = info['end_date']
        source = info['source']

        cur = conn.cursor()
        #cur.execute("SELECT link FROM ArticleData WHERE (title LIKE '%{}%' OR text LIKE '%{}%') AND year IN ({},{}) AND source = '{}';".format(text, text, sdate, edate, source))
        #data = cur.fetchall()

        #credentials = "mysql://admin:group72021@final-project-fe595-group7.cz2xzj6pvabe.us-east-2.rds.amazonaws.com:3306/FinalprojectFE595Group7"
        d1 = pd.read_sql("SELECT link FROM ArticleData WHERE (title LIKE '%{}%' OR text LIKE '%{}%') AND year IN ({},{}) AND source = '{}';".format(text, text, sdate, edate, source),con = conn)

        h1 = d1.shape[0]

        if(h1==0):
            flash('No articles found in database, try another source.')
            return redirect(url_for('home'))
        else:


            #html = d1.to_html(render_links=True, escape=False)
            #text_file = open("templates/results.html", "w")
            #text_file.write(html)
            #text_file.close()

            return render_template('results.html', name = d1)

    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
