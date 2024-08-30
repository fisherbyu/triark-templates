
--
-- Data for Name: code_block; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.code_block (title, content, "empID_id", type_id) FROM stdin;
\.

'
--
-- Data for Name: content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.content_type (title) FROM stdin;
signature
email content
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee ("empID", first_name, last_name, phone_number, email) FROM stdin;
1	Jay	Hancock	9167249537	triarkroofing@gmail.com
0	TRIARK	ROOFING	9162350462	fisherandrew777@gmail.com
2	Barbara	Fisher	9169839839	bjdfisher@sbcglobal.net
3	Camilla	Hancock	9169557516	triarkcamilla@gmail.com
\.


--
-- Data for Name: header_block; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.header_block (title, content) FROM stdin;
head	<!DOCTYPE html>\r\n<html lang="en">\r\n\r\n<head>\r\n\t<meta charset="UTF-8">\r\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n\t<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">\r\n</head>\r\n<div style="font-family: 'Roboto', sans-serif; font-size: 14pt; color: black;">\r\n\t<div class="brd_bar top_bar" style="width: 100%; margin: auto; background-color: black; height: 25pt;"></div>\r\n\t<br>\r\n\t<img class="headicon" style="width: 200px; margin: auto; display: block;"\r\n\t\tsrc="https://app.jobnimbus.com/api1/files/lhgsj2ati2bltxqjckawpim" alt="" />\r\n\t<br />\r\n\t<br>
footer	<br>\r\n\t<div style="width: 100%; margin: auto; background-color: black; display: flex;">\r\n\t\t<p style="width: 60%; margin: auto; color: white; font-size: small; text-align: center; padding: 3pt;">\r\n\t\t\t961 Washington Blvd\r\n\t\t\t<br>\r\n\t\t\tSuite 601\r\n\t\t\t<br>\r\n\t\t\tRoseville, CA\r\n\t\t\t<br>\r\n\t\t\t(916) 276-8632\r\n\t\t\t<br>\r\n\t\t\t<a style="color: white; text-decoration: none;" href="https://www.triarkroofing.com">triarkroofing.com</a>\r\n\t\t</p>\r\n\t</div>\r\n</div>\r\n\r\n</html>
\.

