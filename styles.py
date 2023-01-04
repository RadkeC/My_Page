style = """
html {
    --color_first: #FCB103;
    --color_second: #FF0000;
}

/* hide scrollbar */
html::-webkit-scrollbar {
    display: none;
}
html {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

body {
	height: 100%;
	width: 100%;

	margin: 0;
	padding: 0;

	background-color: var(--color_first);   
}

.section_footer {
	width: 100%;
	height: 30px;
	margin-top: 10px;

	border-style: solid;
	border-width: 6px 0 0 0;
	border-color: var(--color_second);
	box-sizing: border-box;
}

.p_footer{
    float: right;
    margin: 0;
    padding: 0 3px;;
}

.section_content_inside {
	height: calc(100vh - 40px);
	width: 100vw;
	padding: 30px;
	
	overflow: scroll;
	
	box-sizing: border-box;
}

/* hide scrollbar */
.section_content_inside::-webkit-scrollbar {
    display: none;
}
.section_content_inside {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.section_person_header {
    text-align: center;
}

.div_person_header {
	padding: 10px;

	border-style: solid;
	border-width: 3px;
	border-color: var(--color_second);
	box-sizing: border-box;
	border-radius: 5px;
}

.section_projects {
    width: calc(100vw - 60px);
    margin-top: 30px;
    
    position: relative;  
}

.section_main_projects, .section_small_projects {
    float: left;

    width: calc(50% - 15px);
    
    border-style: solid;
    border-width: 3px;
    border-color: var(--color_second);
    box-sizing: border-box;
    border-radius: 5px;
}

.section_small_projects {
    margin-left: 30px;
}

h3 {
    text-align: center;
    padding-bottom: 10px;
    
    border-style: dashed;
    border-width: 0 0 3px 0;
    border-color: var(--color_second);
    box-sizing: border-box;
}

.div_main_projects, .div_small_projects {
    margin: 3px;
    padding: 3px;

    border-style: solid;
    border-width: 1px;
    border-color: var(--color_second);
    box-sizing: border-box;
    border-radius: 5px;
}

h4 {
    text-align: center;
}

"""
