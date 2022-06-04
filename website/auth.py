from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import client
from .models import OrganizationsForm, worksForm, belongs_to2Form, works2Form, ResearchersForm, HFRI_departmentForm, Financial_ProgrammeForm, HFRI_executivesForm, ProjectsForm, Organization_AddressForm, Organization_TelephoneForm, CompanyForm, UniversityForm, Research_CenterForm, final_productForm, scientific_fieldForm, belongs_toForm, evaluateForm, evaluate2Form, Organization_TelephoneForm2
from website.models import OrganizationsForm
from datetime import datetime, timedelta

auth = Blueprint('auth', __name__)

@auth.route('/queries')
def queries():
    return render_template("Queries.html")

@auth.route('/queries/query1')
def query1():
    return render_template("view_projects.html")

@auth.route('/queries/query2')
def query2():
    return render_template("views.html")

@auth.route('/queries/query3')
def query3():
    return render_template("interesting_field.html")

@auth.route('/queries/query3/Aero_Hydro')
def Aero_Hydro():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Aerodynamics & Hydrodynamics" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Aero_Hydro.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query3/Agricultural')
def Agricultural():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Agricultural Science" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Agricultural.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query3/Bio_Health')
def Bio_Health():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Biology & Health" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Bio_Health.html", list1 = list1, list2 = list2, list3 = list3, length = length)  

@auth.route('/queries/query3/Comp_Engineering')
def Comp_Engineering():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Computer Engineering" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Comp_Engineering.html", list1 = list1, list2 = list2, list3 = list3, length = length)  

@auth.route('/queries/query3/Managment')
def Managment():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Managment" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Managment.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query3/Math_Comp')
def Math_Comp():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Math & Computer Science" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Math_Comp.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query3/Physics')
def Physics():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Physics" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Physics.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query3/Power_Env')
def Power_Env():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Power & Environment" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Power_Env.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query3/Social')
def Social():
    cursor = client.cursor()
    cursor.execute("""SELECT projects.project_title, researchers.first_name, researchers.last_name
FROM (((projects JOIN works ON projects.project_ID = works.project_ID)
	  JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
	  JOIN belongs_to ON belongs_to.project_ID = projects.project_ID)
WHERE (belongs_to.scientific_field = "Social Science" AND projects.project_due_date > CURDATE());
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("Social.html", list1 = list1, list2 = list2, list3 = list3, length = length)




@auth.route('/queries/query4')
def query4():
    cursor = client.cursor()
    cursor.execute("""DROP TEMPORARY TABLE IF EXISTS temp;
CREATE TEMPORARY TABLE temp 
SELECT O_name, first_year, (proj_first + proj_second) AS CNT
FROM (
SELECT DISTINCT organizations.org_ID as fav_id, organizations.org_name AS O_name, YEAR(projects.project_starting_date) as first_year, (
					SELECT COUNT(*)
                    FROM projects
                    WHERE (YEAR(projects.project_starting_date) = first_year AND projects.org_ID = fav_id)
                    ) AS proj_first, (
                    SELECT COUNT(*)
                    FROM projects
                    WHERE (YEAR(projects.project_starting_date) = first_year + 1 AND projects.org_ID = fav_id)
                    ) AS proj_second
FROM projects JOIN organizations ON organizations.org_ID = projects.org_ID
HAVING proj_first > 2 AND proj_second > 2
ORDER BY fav_id) T;
    """)
    cursor.execute("""SELECT T1.O_name, T2.O_name, T1.first_year, T2.CNT FROM temp T1 JOIN temp T2 ON (T1.first_year = T2.first_year AND T1.CNT = T2.CNT AND T1.O_name < T2.O_name)
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4 = zip(*results)
    length = len(list1)
    
    return render_template("consecutive_years.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, length = length)

@auth.route('/queries/query5')
def query5():
    cursor = client.cursor()
    cursor.execute("""SELECT temp.SF1, temp.SF2, COUNT(temp.PR) AS CNT
FROM (
SELECT distinct F1.scientific_field AS SF1, F2.scientific_field AS SF2, F1.project_ID AS PR
	FROM belongs_to AS F1, belongs_to AS F2
    WHERE (F1.project_ID = F2.project_ID AND F1.scientific_field < F2.scientific_field) 
    ORDER BY F1.project_ID
   ) temp
GROUP BY temp.SF1, temp.SF2
ORDER BY CNT DESC 
LIMIT 3
 ;
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("top3_fields.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query6')
def query6():
    cursor = client.cursor()
    cursor.execute("""SELECT temp.RESEARCHER_LAST_NAME, temp.RESEARCHER_FIRST_NAME, COUNT(temp.PROJECT_ID) AS CNT
FROM (
	SELECT 
		researchers.last_name AS RESEARCHER_LAST_NAME,
		researchers.FIRST_name AS RESEARCHER_FIRST_NAME,
		researchers.researcher_ID AS RESEARCHER_ID,
		projects.project_ID AS PROJECT_ID
		FROM (researchers JOIN works ON researchers.researcher_ID = works.researcher_ID) 
			JOIN projects ON projects.project_ID = works.project_ID
        WHERE researchers.age < 40 and CURDATE() < projects.project_due_date
	) temp
GROUP BY temp.RESEARCHER_LAST_NAME, temp.RESEARCHER_FIRST_NAME
ORDER BY CNT DESC
;
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("young_researchers.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query7')
def query7():
    cursor = client.cursor()
    cursor.execute("""SELECT T.LN , T.FN , SUM(T.capital) AS TotalCapital
      FROM (SELECT HFRI_executives.executive_last_name AS LN , HFRI_executives.executive_first_name AS FN , company.capital AS capital
			FROM (HFRI_executives JOIN projects ON projects.supervisor_executive_ID = HFRI_executives.executive_ID)
			JOIN company ON company.org_ID = projects.org_ID 
			) as T
      GROUP BY T.LN
      ORDER BY TotalCapital DESC
      LIMIT 5;
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("top5_executives.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query8')
def query8():
    cursor = client.cursor()
    cursor.execute("""SELECT TEMP.FirstName, TEMP.LastName, TEMP.NumProj
FROM(
	(SELECT T.FN AS FirstName, T.LN AS LastName, COUNT(T.PID) AS NumProj
	FROM(
		(SELECT researchers.first_name AS FN, researchers.last_name AS LN, works.project_ID AS PID
		FROM (researchers JOIN works ON researchers.researcher_ID = works.researcher_ID)
		WHERE works.project_ID NOT IN (SELECT final_product.project_ID FROM final_product)
		ORDER BY works.project_ID) AS T
		) 
	GROUP BY T.FN, T.LN) AS TEMP
    )
WHERE (TEMP.NumProj >= '5');

    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)


    return render_template("more_researchers.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/CRUD')
def CRUD():
    return render_template("CRUD.html")   

@auth.route('/queries/query2/view1')
def view1():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM view_projects_researcher;
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("view1.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/queries/query2/view2')
def view2():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM view_projects_sf;
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2 = zip(*results)
    length = len(list1)
    
    return render_template("view2.html", list1 = list1, list2 = list2, length = length)    
  
@auth.route('/queries/query1/all')
def all():
    return render_template("all.html")  

@auth.route('/queries/query1/no_starting_date')
def no_starting_date():
    return render_template("no_starting_date.html")  

@auth.route('/queries/query1/no_exec')
def no_exec():
    return render_template("no_exec.html")  

@auth.route('/queries/query1/no_duration')
def no_duration():
    return render_template("no_duration.html")  

@auth.route('/queries/query1/only_duration')
def only_duration():
    return render_template("only_duration.html")  

@auth.route('/queries/query1/only_exec')
def only_exec():
    return render_template("only_exec.html")  

@auth.route('/queries/query1/only_starting_date')
def only_starting_date():
    return render_template("only_starting_date.html")     

@auth.route('/queries/query1/all/all_by_title')
def all_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title

    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7, list8 = zip(*results)
    length = len(list1)
    
    return render_template("all_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, list8 = list8, length = length)

@auth.route('/queries/query1/all/all_by_starting_date')
def all_by_starting_date():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_starting_date
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7, list8 = zip(*results)
    length = len(list1)
    
    return render_template("all_by_starting_date.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, list8 = list8, length = length)

@auth.route('/queries/query1/all/all_by_exec')
def all_by_exec():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY HFRI_executives.executive_first_name, HFRI_executives.executive_last_name
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7, list8 = zip(*results)
    length = len(list1)
    
    return render_template("all_by_exec.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, list8 = list8, length = length)

@auth.route('/queries/query1/all/all_by_duration')
def all_by_duration():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.duration
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7, list8 = zip(*results)
    length = len(list1)
    
    return render_template("all_by_duration.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7= list7, list8 = list8, length = length)

@auth.route('/queries/query1/no_duration/no_duration_by_title')
def no_duration_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7 = zip(*results)
    length = len(list1)
    
    return render_template("no_duration_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, length = length)

@auth.route('/queries/query1/no_duration/no_duration_by_starting_date')
def no_duration_by_starting_date():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_starting_date
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7 = zip(*results)
    length = len(list1)
    
    return render_template("no_duration_by_starting_date.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, length = length)

@auth.route('/queries/query1/no_duration/no_duration_by_exec')
def no_duration_by_exec():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.project_starting_date AS STARTING_DATE,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY HFRI_executives.executive_first_name, HFRI_executives.executive_last_name
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7 = zip(*results)
    length = len(list1)
    
    return render_template("no_duration_by_exec.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, length = length)

@auth.route('/queries/query1/no_exec/no_exec_by_title')
def no_exec_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.project_starting_date AS STARTING_DATE,
	projects.duration AS DURATION,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6 = zip(*results)
    length = len(list1)
    
    return render_template("no_exec_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, length = length)

@auth.route('/queries/query1/no_exec/no_exec_by_duration')
def no_exec_by_duration():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.project_starting_date AS STARTING_DATE,
	projects.duration AS DURATION,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.duration
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6 = zip(*results)
    length = len(list1)
    
    return render_template("no_exec_by_duration.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, length = length)

@auth.route('/queries/query1/no_exec/no_exec_by_starting_date')
def no_exec_by_starting_date():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.project_starting_date AS STARTING_DATE,
	projects.duration AS DURATION,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_starting_date
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6 = zip(*results)
    length = len(list1)
    
    return render_template("no_exec_by_starting_date.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, length = length)


@auth.route('/queries/query1/no_starting_date/no_starting_date_by_title')
def no_starting_date_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7 = zip(*results)
    length = len(list1)
    
    return render_template("no_starting_date_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, length = length)

@auth.route('/queries/query1/no_starting_date/no_starting_date_by_duration')
def no_starting_date_by_duration():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.duration

""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7 = zip(*results)
    length = len(list1)
    
    return render_template("no_starting_date_by_duration.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, length = length)

@auth.route('/queries/query1/no_starting_date/no_starting_date_by_exec')
def no_starting_date_by_exec():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	projects.duration AS DURATION,
    HFRI_executives.executive_first_name AS EXEC_FIRST_NAME,
    HFRI_executives.executive_last_name AS EXEC_LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY hfri_executives.executive_first_name, HFRI_executives.executive_last_name
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7 = zip(*results)
    length = len(list1)
    
    return render_template("no_starting_date_by_exec.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, list7 = list7, length = length)


@auth.route('/queries/query1/only_duration/only_duration_by_title')
def only_duration_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.duration AS DURATION,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5 = zip(*results)
    length = len(list1)
    
    return render_template("only_duration_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, length = length)

@auth.route('/queries/query1/only_duration/only_duration_by_duration')
def only_duration_by_duration():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.duration AS DURATION,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.duration
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5 = zip(*results)
    length = len(list1)
    
    return render_template("only_duration_by_duration.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, length = length)

@auth.route('/queries/query1/only_exec/only_exec_by_title')
def only_exec_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	HFRI_executives.executive_first_name AS FIRTS_NAME,
    HFRI_executives.executive_last_name AS LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6 = zip(*results)
    length = len(list1)
    
    return render_template("only_exec_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, length = length)

@auth.route('/queries/query1/only_exec/only_exec_by_exec')
def only_exec_by_exec():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
	HFRI_executives.executive_first_name AS FIRTS_NAME,
    HFRI_executives.executive_last_name AS LAST_NAME,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY HFRI_executives.executive_first_name, HFRI_executives.executive_last_name
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6 = zip(*results)
    length = len(list1)
    
    return render_template("only_exec_by_exec.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, list6 = list6, length = length)


@auth.route('/queries/query1/only_starting_date/only_starting_date_by_title')
def only_starting_date_by_title():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.project_starting_date AS STARTING_DATE,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5 = zip(*results)
    length = len(list1)
    
    return render_template("only_starting_date_by_title.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, length = length)

@auth.route('/queries/query1/only_starting_date/only_starting_date_by_starting_date')
def only_starting_date_by_starting_date():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    projects.project_starting_date AS STARTING_DATE,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_starting_date
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5 = zip(*results)
    length = len(list1)
    
    return render_template("only_starting_date_by_starting_date.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, length = length)


@auth.route('/queries/query1/plain')
def plain():
    cursor = client.cursor()
    cursor.execute("""SELECT
	projects.project_title AS TITLE,
    financial_programme.programme_ID AS PROGRAMME_ID,
    researchers.first_name AS FIRST_NAME,
    researchers.last_name AS LAST_NAME
FROM ((((financial_programme JOIN projects ON financial_programme.programme_ID = projects.programme_ID)
JOIN HFRI_executives ON PROJECTS.supervisor_executive_ID = HFRI_executives.executive_ID)
JOIN works ON projects.project_ID = works.project_ID)
JOIN researchers ON works.researcher_ID = researchers.researcher_ID)
ORDER BY projects.project_title
""")
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4 = zip(*results)
    length = len(list1)
    
    return render_template("plain.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, length = length)


#CRUD


@auth.route('/CRUD/insert')
def insert():
    return render_template("insert.html")   


@auth.route('/CRUD/update')
def update():
    return render_template("update.html")       


@auth.route('/CRUD/delete')
def delete():
    return render_template("delete.html") 


#@auth.route('/CRUD/insert/organizations_insert')
#def organizations_insert():
#    return render_template("organizations_insert.html")   


@auth.route('/CRUD/insert/organizations_insert', methods = ["GET", "POST"])
def insert_organization():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            org_name = request.form.get('org_name')
            org_acronym = request.form.get('org_acronym')
            if(len(org_ID) < 1 or len(org_name) < 1 or len(org_acronym) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:    
                new_organization = OrganizationsForm(org_ID = org_ID, org_name = org_name, org_acronym = org_acronym)
                query = "INSERT INTO organizations(org_ID, org_name, org_acronym) VALUES ('{}', '{}', '{}');".format(new_organization['org_ID'].data, new_organization['org_name'].data, new_organization['org_acronym'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("organizations_insert.html")



@auth.route('/CRUD/insert/researchers_insert', methods = ["GET", "POST"])
def researchers_insert():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            gender = request.form.get('gender')
            birth_date = request.form.get('birth_date')
            org_ID = request.form.get('org_ID')
            employment_starting_date = request.form.get('employment_starting_date')
            if(len(researcher_ID) < 1 or len(first_name) < 1 or len(last_name) < 1 or len(gender) < 1 or len(birth_date) < 1 or len(org_ID) < 1 or len(employment_starting_date) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_researcher = ResearchersForm(researcher_ID = researcher_ID, first_name = first_name, last_name = last_name, gender = gender, birth_date = birth_date, org_ID = org_ID, employment_starting_date = employment_starting_date)
                query = "INSERT INTO researchers(researcher_ID, first_name, last_name, gender, birth_date, org_ID, employment_starting_date, age) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', CONCAT(FLOOR((TIMESTAMPDIFF(MONTH, '{}', CURDATE()) / 12)), ' YEARS ', MOD(TIMESTAMPDIFF(MONTH, '{}', CURDATE()), 12) , ' MONTHS'));".format(new_researcher['researcher_ID'].data, new_researcher['first_name'].data, new_researcher['last_name'].data, new_researcher['gender'].data, new_researcher['birth_date'].data, new_researcher['org_ID'].data, new_researcher['employment_starting_date'].data, new_researcher['birth_date'].data, new_researcher['birth_date'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("researchers_insert.html")    

@auth.route('/CRUD/insert/HFRI_department_insert', methods = ["GET", "POST"])
def HFRi_department_insert():
    if(request.method == "POST"):
        try:
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            HFRI_department_name = request.form.get('HFRI_department_name')
            if(len(HFRI_department_ID) < 1 or len(HFRI_department_name) < 1 ):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_HFRI_department = HFRI_departmentForm(HFRI_department_ID = HFRI_department_ID, HFRI_department_name = HFRI_department_name)
                query = "INSERT INTO HFRI_department(HFRI_department_ID, HFRI_department_name) VALUES ('{}', '{}');".format(new_HFRI_department['HFRI_department_ID'].data, new_HFRI_department['HFRI_department_name'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("HFRI_department_insert.html") 

@auth.route('/CRUD/insert/financial_programme_insert', methods = ["GET", "POST"])
def financial_programme_insert():
    if(request.method == "POST"):
        try:
            programme_ID = request.form.get('programme_ID')
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            if(len(programme_ID) < 1 or len(HFRI_department_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_financial_programme = Financial_ProgrammeForm(programme_ID = programme_ID, HFRI_department_ID = HFRI_department_ID)
                query = "INSERT INTO financial_programme(programme_ID, HFRI_department_ID) VALUES ('{}', '{}');".format(new_financial_programme['programme_ID'].data, new_financial_programme['HFRI_department_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("financial_programme_insert.html")   


@auth.route('/CRUD/insert/HFRI_executives_insert', methods = ["GET", "POST"])
def HFRI_executives_insert():
    if(request.method == "POST"):
        try:
            executive_ID = request.form.get('executive_ID')
            executive_first_name = request.form.get('executive_first_name')
            executive_last_name = request.form.get('executive_last_name')
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            if(len(executive_ID) < 1 or len(executive_first_name) < 1 or len(executive_last_name) < 1 or len(HFRI_department_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_HFRI_executive = HFRI_executivesForm(executive_ID = executive_ID, executive_first_name = executive_first_name, executive_last_name = executive_last_name, HFRI_department_ID = HFRI_department_ID)
                query = "INSERT INTO HFRI_executives(executive_ID, executive_first_name, executive_last_name, HFRI_department_ID) VALUES ('{}', '{}', '{}', '{}');".format(new_HFRI_executive['executive_ID'].data, new_HFRI_executive['executive_first_name'].data, new_HFRI_executive['executive_last_name'].data, new_HFRI_executive['HFRI_department_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("HFRI_executives_insert.html")    

@auth.route('/CRUD/insert/projects_insert', methods = ["GET", "POST"])
def projects_insert():
    if(request.method == "POST"):
        try:
            project_ID = request.form.get('project_ID')
            project_title = request.form.get('project_title')
            project_starting_date = request.form.get('project_starting_date')
            project_summary = request.form.get('project_summary')
            project_due_date = request.form.get('project_due_date')
            supervisor_executive_ID = request.form.get('supervisor_executive_ID')
            supervisor_researcher_ID = request.form.get('supervisor_researcher_ID')
            org_ID = request.form.get('org_ID')
            capital =  request.form.get('capital')
            programme_ID = request.form.get('programme_ID')
            if(len(project_ID) < 1 or len(project_title) < 1 or len(project_starting_date) < 1 or len(project_due_date) < 1 or len(project_summary) < 1 or len(supervisor_executive_ID) < 1 or len(supervisor_researcher_ID) < 1 or len(org_ID) < 1 or len(capital) < 1 or len(programme_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
                dt1 = datetime.strptime(project_starting_date, '%Y-%m-%d').date()
                dt2 = datetime.strptime(project_due_date, '%Y-%m-%d').date()
                dt = dt2 - dt1
                if (dt < timedelta(days = 365) or dt > timedelta(days = 1461)):
                    flash('Duration of the project must be a value between one and four years', category = 'error')
                elif (int(capital) > 1000000 or int(capital) < 100000):
                    flash('Capital of the project must be a value between 100000 and 1000000', category = 'error')
                else:  
                    new_project = ProjectsForm(project_ID = project_ID, project_title = project_title, project_starting_date = project_starting_date, project_summary = project_summary, project_due_date = project_due_date, supervisor_executive_ID = supervisor_executive_ID, supervisor_researcher_ID = supervisor_researcher_ID, org_ID = org_ID, capital = capital, programme_ID = programme_ID)  
                    query = "INSERT INTO projects(project_ID, project_title, project_starting_date, project_summary, project_due_date, supervisor_executive_ID, supervisor_researcher_ID, org_ID, capital, programme_ID, duration) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', TIMESTAMPDIFF(YEAR,'{}','{}'));".format(new_project['project_ID'].data, new_project['project_title'].data, new_project['project_starting_date'].data, new_project['project_summary'].data, new_project['project_due_date'].data, new_project['supervisor_executive_ID'].data, new_project['supervisor_researcher_ID'].data, new_project['org_ID'].data, new_project['capital'].data, new_project['programme_ID'].data, new_project['project_starting_date'].data, new_project['project_due_date'].data)
                    cursor = client.cursor()
                    cursor.execute(query)
                    client.commit()
                    cursor.close()
                    flash('Tuple inserted successfully', category = 'success')
                    return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("projects_insert.html")       

@auth.route('/CRUD/insert/organization_address_insert', methods = ["GET", "POST"])
def organization_address_insert():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            street = request.form.get('street')
            st_number = request.form.get('st_number')
            ZIP_code = request.form.get('ZIP_code')
            city = request.form.get('city')
            if(len(org_ID) < 1 or len(street) < 1 or len(st_number) < 1 or len(ZIP_code) < 1 or len(city) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_organization_address = Organization_AddressForm(org_ID = org_ID, street = street, st_number = st_number, ZIP_code = ZIP_code, city = city)
                query = "INSERT INTO organization_address(org_ID, street, st_number, ZIP_code, city) VALUES ('{}', '{}', '{}', '{}', '{}');".format(new_organization_address['org_ID'].data, new_organization_address['street'].data, new_organization_address['st_number'].data, new_organization_address['ZIP_code'].data, new_organization_address['city'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("organization_address_insert.html")   


@auth.route('/CRUD/insert/organization_telephone_insert', methods = ["GET", "POST"])
def organization_telephone_insert():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            telephone = request.form.get('telephone')
            if(len(org_ID) < 1 or len(telephone) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_organization_telephone = Organization_TelephoneForm(org_ID = org_ID, telephone = telephone)
                query = "INSERT INTO organization_telephone(org_ID, telephone) VALUES ('{}', '{}');".format(new_organization_telephone['org_ID'].data, new_organization_telephone['telephone'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("organization_telephone_insert.html")    

@auth.route('/CRUD/insert/company_insert', methods = ["GET", "POST"])
def company_insert():
    if(request.method == "POST"):
        try:
            company_ID = request.form.get('company_ID')
            capital = request.form.get('capital')
            org_ID = request.form.get('org_ID')
            if(len(company_ID) < 1 or len(capital) < 1 or len(org_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_company = CompanyForm(company_ID = company_ID, capital = capital, org_ID = org_ID)
                query = "INSERT INTO company(company_ID, capital, org_ID) VALUES ('{}', '{}', '{}');".format(new_company['company_ID'].data, new_company['capital'].data, new_company['org_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("company_insert.html")    

@auth.route('/CRUD/insert/university_insert', methods = ["GET", "POST"])
def university_insert():
    if(request.method == "POST"):
        try:
            university_ID = request.form.get('university_ID')
            ministry_budget = request.form.get('ministry_budget')
            org_ID = request.form.get('org_ID')
            if(len(university_ID) < 1 or len(ministry_budget) < 1 or len(org_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_university = UniversityForm(university_ID = university_ID, ministry_budget = ministry_budget, org_ID = org_ID)
                query = "INSERT INTO university(university_ID, ministry_budget, org_ID) VALUES ('{}', '{}', '{}');".format(new_university['university_ID'].data, new_university['ministry_budget'].data, new_university['org_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("university_insert.html")   


@auth.route('/CRUD/insert/research_center_insert', methods = ["GET", "POST"])
def research_center_insert():
    if(request.method == "POST"):
        try:
            research_center_ID = request.form.get('research_center_ID')
            ministry_budget = request.form.get('ministry_budget')
            private_budget = request.form.get('private_budget')
            org_ID = request.form.get('org_ID')
            if(len(research_center_ID) < 1 or len(ministry_budget) < 1 or len(private_budget) < 1 or len(org_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_research_center = Research_CenterForm(research_center_ID = research_center_ID, ministry_budget = ministry_budget, private_budget = private_budget, org_ID = org_ID)
                query = "INSERT INTO research_center(research_center_ID, ministry_budget, private_budget, org_ID) VALUES ('{}', '{}', '{}', '{}');".format(new_research_center['research_center_ID'].data, new_research_center['ministry_budget'].data, new_research_center['private_budget'].data, new_research_center['org_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("research_center_insert.html")    

@auth.route('/CRUD/insert/final_product_insert', methods = ["GET", "POST"])
def final_product_insert():
    if(request.method == "POST"):
        try:
            product_ID = request.form.get('product_ID')
            product_title = request.form.get('product_title')
            project_ID = request.form.get('project_ID')
            product_summary = request.form.get('product_summary')
            product_due_date = request.form.get('product_due_date')
            if(len(product_ID) < 1 or len(product_title) < 1 or len(project_ID) < 1 or len(product_summary) < 1 or len(product_due_date) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_final_product = final_productForm(product_ID = product_ID, product_title = product_title, project_ID = project_ID, product_summary = product_summary, product_due_date = product_due_date)
                query = "INSERT INTO final_product(product_ID, product_title, project_ID, product_summary, product_due_date) VALUES ('{}', '{}', '{}', '{}', '{}');".format(new_final_product['product_ID'].data, new_final_product['product_title'].data, new_final_product['project_ID'].data, new_final_product['product_summary'].data, new_final_product['product_due_date'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("final_product_insert.html")

@auth.route('/CRUD/insert/scientific_field_insert', methods = ["GET", "POST"])
def scientific_field_insert():
    if(request.method == "POST"):
        try:
            scientific_field_name = request.form.get('scientific_field_name')
            if(len(scientific_field_name) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_scientific_field = scientific_fieldForm(scientific_field_name = scientific_field_name)
                query = "INSERT INTO scientific_field(scientific_field_name) VALUES ('{}');".format(new_scientific_field['scientific_field_name'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("scientific_field_insert.html")    

@auth.route('/CRUD/insert/works_insert', methods = ["GET", "POST"])
def works_insert():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            project_ID = request.form.get('project_ID')
            if(len(researcher_ID) < 1 or len(project_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_works = worksForm(researcher_ID = researcher_ID, project_ID = project_ID)
                query = "INSERT INTO works(researcher_ID, project_ID) VALUES ('{}', '{}');".format(new_works['researcher_ID'].data,  new_works['project_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("works_insert.html")   


@auth.route('/CRUD/insert/belongs_to_insert', methods = ["GET", "POST"])
def belongs_to_insert():
    if(request.method == "POST"):
        try:
            scientific_field = request.form.get('scientific_field')
            project_ID = request.form.get('project_ID')
            if(len(scientific_field) < 1 or len(project_ID) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_belongs_to = belongs_toForm(scientific_field = scientific_field, project_ID = project_ID)
                query = "INSERT INTO belongs_to(scientific_field, project_ID) VALUES ('{}', '{}');".format(new_belongs_to['scientific_field'].data,  new_belongs_to['project_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("belongs_to_insert.html")    

@auth.route('/CRUD/insert/evaluate_insert', methods = ["GET", "POST"])
def evaluate_insert():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            project_ID = request.form.get('project_ID')
            grade = request.form.get('grade')
            evaluation_date = request.form.get('evaluation_date')
            if(len(researcher_ID) < 1 or len(project_ID) < 1 or len(grade) < 1 or len(evaluation_date) < 1):
                flash('Do not leave brackets empty, please.', category = 'error')
            else:
                new_evaluate = evaluateForm(researcher_ID = researcher_ID, project_ID = project_ID, grade = grade, evaluation_date = evaluation_date)
                query = "INSERT INTO evaluate(researcher_ID, project_ID, grade, evaluation_date) VALUES ('{}', '{}', '{}', '{}');".format(new_evaluate['researcher_ID'].data, new_evaluate['project_ID'].data, new_evaluate['grade'].data, new_evaluate['evaluation_date'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple inserted successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("evaluate_insert.html")    


#DELEEEEEETE


@auth.route('/CRUD/delete/organizations_delete', methods = ["GET", "POST"])
def organizations_delete():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            query = f"delete from organizations where org_ID='{org_ID}';"
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')        
    return render_template("organizations_delete.html")

@auth.route('/CRUD/delete/researchers_delete', methods = ["GET", "POST"] )
def reserchears_delete():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            query = f"delete from researchers where researcher_ID='{researcher_ID}';"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("researchers_delete.html")

@auth.route('/CRUD/delete/HFRI_department_delete', methods = ["GET", "POST"])
def HFRI_department_delete():
    if(request.method == "POST"):
        try:
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            query = f"delete from HFRI_department where HFRI_department_ID='{HFRI_department_ID}';"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("HFRI_department_delete.html")

@auth.route('/CRUD/delete/financial_programme_delete', methods = ["GET", "POST"])
def financial_programme_delete():
    if(request.method == "POST"):
        try:
            programme_ID = request.form.get('programme_ID')
            query = f"delete from financial_programme where programme_ID='{programme_ID}';"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("financial_programme_delete.html")

@auth.route('/CRUD/delete/HFRI_executives_delete', methods = ["GET", "POST"])
def HFRI_executives_delete():
    if(request.method == "POST"):
        try:
            executive_ID = request.form.get('executive_ID')
            query = f"delete from HFRI_executives where executive_ID='{executive_ID}';"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("HFRI_executives_delete.html")

@auth.route('/CRUD/delete/projects_delete', methods = ["GET", "POST"])
def projects_delete():
    if(request.method == "POST"):
        try:
            project_ID = request.form.get('project_ID')
            query = f"delete from projects where project_ID='{project_ID}';"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("projects_delete.html")

@auth.route('/CRUD/delete/organization_address_delete', methods = ["GET", "POST"])
def organization_address_delete():
    if(request.method == "POST"):
        try:
            street = request.form.get('street')
            st_number = request.form.get('st_number')
            ZIP_code = request.form.get('ZIP_code')
            city = request.form.get('city')
            org_id = request.form.get('org_id')
            query = f"delete from organization_address where street='{street}' and st_number='{st_number}' and ZIP_code='{ZIP_code}' and city='{city}' and org_id='{org_id}';"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("organization_address_delete.html")

@auth.route('/CRUD/delete/organization_telephone_delete', methods = ["GET", "POST"])
def organization_telephone_delete():
    if(request.method == "POST"):
        try:
            telephone = request.form.get('telephone')
            query = f"delete from organization_telephone where telephone= '{telephone}'"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("organization_telephone_delete.html")


@auth.route('/CRUD/delete/final_product_delete', methods = ["GET", "POST"])
def final_product_delete():
    if(request.method == "POST"):
        try:
            product_ID = request.form.get('product_ID')
            query = f"delete from final_product where product_ID= '{product_ID}'"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("final_product_delete.html")

#we cannot delete university, company and research center, because they will be deleted by deleting the organization

@auth.route('/CRUD/delete/scientific_field_delete', methods = ["GET", "POST"])
def scientific_field_delete():
    if(request.method == "POST"):
        try:
            scientific_field_name = request.form.get('scientific_field_name')
            query = f"delete from scientific_field where scientific_field_name= '{scientific_field_name}'"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("scientific_field_delete.html")

@auth.route('/CRUD/delete/belongs_to_delete', methods = ["GET", "POST"])
def belongs_to_delete():
    if(request.method == "POST"):
        try:
            scientific_field = request.form.get('scientific_field')
            project_id = request.form.get('project_id')
            query = f" delete from belongs_to where scientific_field='{scientific_field}' and project_id='{project_id}'"
            print(query)
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("belongs_to_delete.html")

@auth.route('/CRUD/delete/works_delete', methods = ["GET", "POST"])
def works_delete():
     if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            project_ID = request.form.get('project_ID')
            query = f"delete from works where researcher_ID='{researcher_ID}' and project_id='{project_ID}'"
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
     return render_template("works_delete.html")

@auth.route('/CRUD/delete/evaluate_delete', methods = ["GET", "POST"])
def evaluate_delete():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            project_ID = request.form.get('project_ID')
            query = f"delete from evaluate where researcher_ID='{researcher_ID}' and project_id='{project_ID}'"
            cursor = client.cursor()
            cursor.execute(query)
            client.commit()
            cursor.close()
            flash('Tuple deleted successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')
    return render_template("evaluate_delete.html")


#UPDAAAAAATE

@auth.route('/CRUD/update/projects_update', methods = ["GET", "POST"])
def projects_update():
    if(request.method == "POST"):
        try:
            project_ID = request.form.get('project_ID')
            project_title = request.form.get('project_title')
            project_starting_date = request.form.get('project_starting_date')
            project_summary = request.form.get('project_summary')
            project_due_date = request.form.get('project_due_date')
            supervisor_executive_ID = request.form.get('supervisor_executive_ID')
            supervisor_researcher_ID = request.form.get('supervisor_researcher_ID')
            org_ID = request.form.get('org_ID')
            capital =  request.form.get('capital')
            programme_ID = request.form.get('programme_ID')
            if(len(project_ID) < 1 or len(project_title) < 1 or len(project_starting_date) < 1 or len(project_due_date) < 1 or len(project_summary) < 1 or len(supervisor_executive_ID) < 1 or len(supervisor_researcher_ID) < 1 or len(org_ID) < 1 or len(capital) < 1 or len(programme_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            dt1 = datetime.strptime(project_starting_date, '%Y-%m-%d').date()
            dt2 = datetime.strptime(project_due_date, '%Y-%m-%d').date()
            dt = dt2 - dt1
            if (dt < timedelta(days = 365) or dt > timedelta(days = 1461)):
                flash('Duration of the project must be a value between one and four years', category = 'error')
            elif (int(capital) > 1000000 or int(capital) < 100000):
                flash('Capital of the project must be a value between 100000 and 1000000', category = 'error')
            else:    
                new_project = ProjectsForm(project_ID = project_ID, project_title = project_title, project_starting_date = project_starting_date, project_summary = project_summary, project_due_date = project_due_date, supervisor_executive_ID = supervisor_executive_ID, supervisor_researcher_ID = supervisor_researcher_ID, org_ID = org_ID, capital = capital, programme_ID = programme_ID)
                query = "update projects set project_title='{}', project_starting_date='{}', project_summary='{}', project_due_date='{}', supervisor_executive_ID='{}', supervisor_researcher_ID='{}', org_id='{}', capital='{}', programme_ID='{}', duration= TIMESTAMPDIFF(YEAR,'{}','{}') where project_ID='{}';".format( new_project['project_title'].data, new_project['project_starting_date'].data, new_project['project_summary'].data, new_project['project_due_date'].data, new_project['supervisor_executive_ID'].data, new_project['supervisor_researcher_ID'].data, new_project['org_ID'].data, new_project['capital'].data, new_project['programme_ID'].data, new_project['project_starting_date'].data, new_project['project_due_date'].data, new_project['project_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("projects_update.html")



@auth.route('/CRUD/update/organizations_update', methods = ["GET", "POST"])
def update_organization():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            org_name = request.form.get('org_name')
            org_acronym = request.form.get('org_acronym')
            if(len(org_ID) < 1 or len(org_name) < 1 or len(org_acronym) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:
                new_organization = OrganizationsForm(org_ID = org_ID, org_name = org_name, org_acronym = org_acronym)
                query = "update organizations set org_name='{}', org_acronym='{}' where org_id='{}';".format( new_organization['org_name'].data, new_organization['org_acronym'].data, new_organization['org_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
            return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("organizations_update.html")






@auth.route('/CRUD/update/researchers_update', methods = ["GET", "POST"])
def researchers_update():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            gender = request.form.get('gender')
            birth_date = request.form.get('birth_date')
            org_ID = request.form.get('org_ID')
            employment_starting_date = request.form.get('employment_starting_date')
            if(len(researcher_ID) < 1 or len(first_name) < 1 or len(last_name) < 1 or len(gender) < 1 or len(birth_date) < 1 or len(org_ID) < 1 or len(employment_starting_date) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_researcher = ResearchersForm(researcher_ID = researcher_ID, first_name = first_name, last_name = last_name, gender = gender, birth_date = birth_date, org_ID = org_ID, employment_starting_date = employment_starting_date)
                query = "update researchers set first_name='{}', last_name='{}', birth_date='{}', gender='{}', org_id='{}', employment_starting_date='{}', age=CONCAT(FLOOR((TIMESTAMPDIFF(MONTH, '{}', CURDATE()) / 12)), ' YEARS ', MOD(TIMESTAMPDIFF(MONTH, '{}', CURDATE()), 12) , ' MONTHS') where researcher_id='{}';".format( new_researcher['first_name'].data, new_researcher['last_name'].data, new_researcher['birth_date'].data, new_researcher['gender'].data, new_researcher['org_ID'].data, new_researcher['employment_starting_date'].data, new_researcher['birth_date'].data, new_researcher['birth_date'].data, new_researcher['researcher_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("researchers_update.html")  

@auth.route('/CRUD/update/HFRI_department_update', methods = ["GET", "POST"])
def HFRi_department_update():
    if(request.method == "POST"):
        try:
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            HFRI_department_name = request.form.get('HFRI_department_name')
            new_HFRI_department = HFRI_departmentForm(HFRI_department_ID = HFRI_department_ID, HFRI_department_name = HFRI_department_name)
            if(len(HFRI_department_ID) < 1 or len(HFRI_department_name) < 1 or len(new_HFRI_department) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                query = "update HFRI_department set HFRI_department_name='{}' where HFRI_department_ID='{}';" .format( new_HFRI_department['HFRI_department_name'].data, new_HFRI_department['HFRI_department_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("HFRI_department_update.html") 




@auth.route('/CRUD/update/financial_programme_update', methods = ["GET", "POST"])
def financial_programme_update():
    if(request.method == "POST"):
        try:
            programme_ID = request.form.get('programme_ID')
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            if(len(programme_ID) < 1 or len(HFRI_department_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_financial_programme = Financial_ProgrammeForm(programme_ID = programme_ID, HFRI_department_ID = HFRI_department_ID)
                query = "update financial_programme set HFRI_department_id='{}' where programme_ID='{}' ; ".format( new_financial_programme['HFRI_department_ID'].data, new_financial_programme['programme_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("financial_programme_update.html")   


@auth.route('/CRUD/update/HFRI_executives_update', methods = ["GET", "POST"])
def HFRI_executives_update():
    if(request.method == "POST"):
        try:
            executive_ID = request.form.get('executive_ID')
            executive_first_name = request.form.get('executive_first_name')
            executive_last_name = request.form.get('executive_last_name')
            HFRI_department_ID = request.form.get('HFRI_department_ID')
            if(len(executive_ID) < 1 or len(executive_first_name) < 1 or len(executive_last_name) < 1 or len(HFRI_department_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_HFRI_executive = HFRI_executivesForm(executive_ID = executive_ID, executive_first_name = executive_first_name, executive_last_name = executive_last_name, HFRI_department_ID = HFRI_department_ID)
                query = "update HFRI_executives set executive_first_name='{}', executive_last_name='{}', HFRI_department_ID='{}' where executive_ID='{}';".format( new_HFRI_executive['executive_first_name'].data, new_HFRI_executive['executive_last_name'].data, new_HFRI_executive['HFRI_department_ID'].data, new_HFRI_executive['executive_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')

    return render_template("HFRI_executives_update.html") 


@auth.route('/CRUD/update/organization_address_update', methods = ["GET", "POST"])
def organization_address_update():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            street = request.form.get('street')
            st_number = request.form.get('st_number')
            ZIP_code = request.form.get('ZIP_code')
            city = request.form.get('city')
            if(len(org_ID) < 1 or len(street) < 1 or len(st_number) < 1 or len(ZIP_code) < 1 or len(city) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_organization_address = Organization_AddressForm(org_ID = org_ID, street = street, st_number = st_number, ZIP_code = ZIP_code, city = city)
                query = "update organization_address set street = '{}', st_number='{}',  ZIP_code='{}',  city='{}' where org_id='{}'; ".format( new_organization_address['street'].data, new_organization_address['st_number'].data, new_organization_address['ZIP_code'].data, new_organization_address['city'].data, new_organization_address['org_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("organization_address_update.html")


@auth.route('/CRUD/update/organization_telephone_update', methods = ["GET", "POST"])
def organization_telephone_update():
    if(request.method == "POST"):
        try:
            org_ID = request.form.get('org_ID')
            telephone = request.form.get('telephone')
            new_telephone=request.form.get('new_telephone')
            if(len(org_ID) < 1 or len(telephone) < 1 or len(new_telephone) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_organization_telephone = Organization_TelephoneForm2(org_ID = org_ID, telephone = telephone, new_telephone = new_telephone)
                query = "update organization_telephone set telephone='{}'  where org_id='{}' and telephone='{}';".format( new_organization_telephone['new_telephone'].data, new_organization_telephone['org_ID'].data, new_organization_telephone['telephone'].data )
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("organization_telephone_update.html")  

  
@auth.route('/CRUD/update/company_update', methods = ["GET", "POST"])
def company_update():
    if(request.method == "POST"):
        try:
            company_ID = request.form.get('company_ID')
            capital = request.form.get('capital')
            org_ID = request.form.get('org_ID')
            if(len(company_ID) < 1 or len(capital) < 1 or len(org_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_company = CompanyForm(company_ID = company_ID, capital = capital, org_ID = org_ID)
                query = "update company set org_ID='{}', capital='{}' where company_id='{}';".format(new_company['company_ID'].data, new_company['capital'].data, new_company['org_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("company_update.html")   



@auth.route('/CRUD/update/university_update', methods = ["GET", "POST"])
def university_update():
    if(request.method == "POST"):
        try:
            university_ID = request.form.get('university_ID')
            ministry_budget = request.form.get('ministry_budget')
            org_ID = request.form.get('org_ID')
            if(len(university_ID) < 1 or len(ministry_budget) < 1 or len(org_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_university = UniversityForm(university_ID = university_ID, ministry_budget = ministry_budget, org_ID = org_ID)
                query = "update university set org_ID='{}', ministry_budget='{}' where university_id='{}';".format( new_university['org_ID'].data, new_university['ministry_budget'].data,  new_university['university_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("university_update.html")  


@auth.route('/CRUD/update/research_center_update', methods = ["GET", "POST"])
def research_center_update():
    if(request.method == "POST"):
        try:
            research_center_ID = request.form.get('research_center_ID')
            ministry_budget = request.form.get('ministry_budget')
            private_budget = request.form.get('private_budget')
            org_ID = request.form.get('org_ID')
            if(len(research_center_ID) < 1 or len(ministry_budget) < 1 or len(private_budget) < 1 or len(org_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_research_center = Research_CenterForm(research_center_ID = research_center_ID, ministry_budget = ministry_budget, private_budget = private_budget, org_ID = org_ID)
                query = "update research_center set org_ID='{}', ministry_budget='{}', private_budget='{}' where research_center_ID='{}';".format( new_research_center['org_ID'].data, new_research_center['ministry_budget'].data, new_research_center['private_budget'].data,  new_research_center['research_center_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("research_center_update.html")  


@auth.route('/CRUD/update/final_product_update', methods = ["GET", "POST"])
def final_product_update():
    if(request.method == "POST"):
        try:
            product_ID = request.form.get('product_ID')
            product_title = request.form.get('product_title')
            project_ID = request.form.get('project_ID')
            product_summary = request.form.get('product_summary')
            product_due_date = request.form.get('product_due_date')
            if(len(product_ID) < 1 or len(product_title) < 1 or len(project_ID) < 1 or len(product_summary) < 1 or len(product_due_date) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_final_product = final_productForm(product_ID = product_ID, product_title = product_title, project_ID = project_ID, product_summary = product_summary, product_due_date = product_due_date)
                query = "update final_product set product_title='{}', project_ID='{}', product_summary='{}', product_due_date='{}' where product_ID='{}';".format( new_final_product['product_title'].data, new_final_product['project_ID'].data, new_final_product['product_summary'].data, new_final_product['product_due_date'].data, new_final_product['product_ID'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("final_product_update.html")




@auth.route('/CRUD/update/works_update', methods = ["GET", "POST"])
def works_update():
    if(request.method == "POST"):
        try:
            researcher_ID = request.form.get('researcher_ID')
            project_ID = request.form.get('project_ID')
            new_researcher_ID = request.form.get('new_researcher_ID')
            new_project_ID = request.form.get('new_project_ID')
            if(len(researcher_ID) < 1 or len(project_ID) < 1 or len(new_researcher_ID) < 1 or len(new_project_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_works = works2Form(researcher_ID = researcher_ID, project_ID = project_ID, new_researcher_ID = new_researcher_ID, new_project_ID = new_project_ID  )
                query = "update works set project_ID='{}', researcher_id='{}' where researcher_ID='{}' and project_id='{}';".format(  new_works['new_project_ID'].data, new_works['new_researcher_ID'].data, new_works['researcher_ID'].data, new_works['project_ID'].data  )
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("works_update.html")   

@auth.route('/CRUD/update/belongs_to_update', methods = ["GET", "POST"])
def belongs_to_update():
    if(request.method == "POST"):
        try:
            scientific_field = request.form.get('scientific_field')
            project_ID = request.form.get('project_ID')
            old_scientific_field=request.form.get('old_scientific_field')
            old_project_ID=request.form.get('old_project_ID')
            if(len(scientific_field) < 1 or len(project_ID) < 1 or len(old_scientific_field) < 1 or len(old_project_ID) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_belongs_to = belongs_to2Form(scientific_field = scientific_field, project_ID = project_ID, old_scientific_field=old_scientific_field, old_project_ID=old_project_ID)
                query = "update belongs_to set scientific_field='{}', project_ID='{}'  where project_id='{}' and scientific_field='{}';".format(new_belongs_to['scientific_field'].data,  new_belongs_to['project_ID'].data, new_belongs_to['old_project_ID'].data, new_belongs_to['old_scientific_field'].data)
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("belongs_to_update.html")    


@auth.route('/CRUD/update/evaluate_update', methods = ["GET", "POST"])
def evaluate_update():
    if(request.method == "POST"):
        try:
            researcher_ID=request.form.get('researcher_ID')
            project_ID=request.form.get('project_ID')
            new_researcher_ID = request.form.get('new_researcher_ID')
            new_project_ID = request.form.get('new_project_ID')
            grade = request.form.get('grade')
            evaluation_date = request.form.get('evaluation_date')
            if(len(researcher_ID) < 1 or len(project_ID) < 1 or len(new_researcher_ID) < 1 or len(new_project_ID) < 1 or len(grade) < 1 or len(evaluation_date) < 1):
                flash('Do not leave brackets empty, please. If you do not want to change some values just put the previous value in the bracket.', category = 'error')
            else:    
                new_evaluate = evaluate2Form(researcher_ID = researcher_ID, project_ID = project_ID, new_researcher_ID = new_researcher_ID, new_project_ID = new_project_ID, grade = grade, evaluation_date = evaluation_date)
                query = "update evaluate set researcher_ID='{}', project_ID='{}', grade='{}', evaluation_date='{}' where researcher_id='{}' and project_id='{}';".format( new_evaluate['new_researcher_ID'].data, new_evaluate['new_project_ID'].data, new_evaluate['grade'].data, new_evaluate['evaluation_date'].data, new_evaluate['researcher_ID'].data, new_evaluate['project_ID'].data) 
                cursor = client.cursor()
                cursor.execute(query)
                client.commit()
                cursor.close()
                flash('Tuple updated successfully', category = 'success')
                return redirect(url_for('auth.CRUD'))
        except Exception as e:
            flash(str(e), category = 'error')


    return render_template("evaluate_update.html")    


@auth.route('/CRUD/read')
def read():
    return render_template("read.html") 

@auth.route('/CRUD/read/organizations_read')
def organizations_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM organizations
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("organizations_read.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/CRUD/read/researchers_read')
def researchers_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM researchers
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7, list8 = zip(*results)
    length = len(list1)
    
    return render_template("researchers_read.html", list1 = list1, list2 = list2, list3 = list3, list4= list4, list5 = list5, list6 = list6, list7 = list7, list8 = list8, length = length)

@auth.route('/CRUD/read/HFRI_department_read')
def HFRI_department_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM HFRI_department
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2 = zip(*results)
    length = len(list1)
    
    return render_template("HFRI_department_read.html", list1 = list1, list2 = list2, length = length)

@auth.route('/CRUD/read/financial_programme_read')
def financial_programme_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM financial_programme
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2 = zip(*results)
    length = len(list1)
    
    return render_template("financial_programme_read.html", list1 = list1, list2 = list2, length = length)

@auth.route('/CRUD/read/HFRI_executives_read')
def HFRI_executives_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM HFRI_executives
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4 = zip(*results)
    length = len(list1)
    
    return render_template("HFRI_executives_read.html", list1 = list1, list2 = list2, list3 = list3, list4= list4, length = length)


@auth.route('/CRUD/read/projects_read')
def projects_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM projects
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11 = zip(*results)
    length = len(list1)
    
    return render_template("projects_read.html", list1 = list1, list2 = list2, list3 = list3, list4= list4, list5 = list5, list6 = list6, list7 = list7, list8 = list8, list9 = list9, list10 = list10, list11 = list11, length = length)


@auth.route('/CRUD/read/organization_address_read')
def organization_address_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM organization_address
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5 = zip(*results)
    length = len(list1)
    
    return render_template("organization_address_read.html", list1 = list1, list2 = list2, list3 = list3, list4= list4, list5 = list5, length = length)

@auth.route('/CRUD/read/organization_telephone_read')
def organization_telephone_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM organization_telephone
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2 = zip(*results)
    length = len(list1)
    
    return render_template("organization_telephone_read.html", list1 = list1, list2 = list2, length = length)

@auth.route('/CRUD/read/company_read')
def company_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM company
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("company_read.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/CRUD/read/university_read')
def university_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM university
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3 = zip(*results)
    length = len(list1)
    
    return render_template("university_read.html", list1 = list1, list2 = list2, list3 = list3, length = length)

@auth.route('/CRUD/read/research_center_read')
def research_center_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM research_center
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4 = zip(*results)
    length = len(list1)
    
    return render_template("research_center_read.html", list1 = list1, list2 = list2, list3 = list3, list4= list4, length = length)

@auth.route('/CRUD/read/final_product_read')
def final_product_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM final_product
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4, list5 = zip(*results)
    length = len(list1)
    
    return render_template("final_product_read.html", list1 = list1, list2 = list2, list3 = list3, list4= list4, list5 = list5, length = length)

@auth.route('/CRUD/read/scientific_field_read')
def scientific_field_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM scientific_field
    """)
    results = cursor.fetchall()
    cursor.close()

    list1 = results
    length = len(list1)
    
    return render_template("scientific_field_read.html", list1 = list1, length = length)

@auth.route('/CRUD/read/belongs_to_read')
def belongs_to_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM belongs_to
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2 = zip(*results)
    length = len(list1)
    
    return render_template("belongs_to_read.html", list1 = list1, list2 = list2, length = length)

@auth.route('/CRUD/read/works_read')
def works_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM works
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2 = zip(*results)
    length = len(list1)
    
    return render_template("works_read.html", list1 = list1, list2 = list2, length = length)

@auth.route('/CRUD/read/evaluates_read')
def evaluates_read():
    cursor = client.cursor()
    cursor.execute("""SELECT * FROM evaluate
    """)
    results = cursor.fetchall()
    cursor.close()

    list1, list2, list3, list4= zip(*results)
    length = len(list1)
    
    return render_template("evaluates_read.html", list1 = list1, list2 = list2, list3 = list3, list4 = list4, length = length)

