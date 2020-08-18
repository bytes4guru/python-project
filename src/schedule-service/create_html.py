'''
Created on Aug 18, 2020
@author: Brennan Brown
'''


from datetime import datetime

def create_html_report(data_dict, icon_url, html_file):

    alt_var = data_dict['weather']

    with open(html_file, mode='w') as outfile:
        outfile.write('<html>\n')
        outfile.write('<head>\n<title>Python Weather HTML</title>\n</head>\n\n')
        outfile.write('<body>\n')
        outfile.write('<div style="margin: 0 auto; width: 40%">\n')
        outfile.write( '<tr><td align="center"> </td></tr><br>\n' )
        outfile.write( '<br><p style="text-align: center;"><b>\n    WEATHER DATA:\n</b></p>\n' )
        outfile.write( '<img style="float: right;" alt={} src={}>\n'.format(alt_var, icon_url))
        outfile.write( '<br>\n\n')

        outfile.write( '<table border=1>\n' )
        #--------------------------------------------
        for key, value in data_dict.items():
            outfile.write( '    <tr><td><b><span style="color:black"> {:s} </b></td><td align="left">\n'.format(key) )
            outfile.write( '    <span style="color:blue"><b> {:s} </b></span></td></tr>\n'.format(value) )
        #--------------------------------------------
        outfile.write( '</table>\n\n' )
        outfile.write( '<p> Generated: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' </p>\n')
        outfile.write('</div>\n')
        outfile.write('</body>\n')
        outfile.write('</html>')

#===========================================
if __name__ == '__main__':
    from weather_data import get_weather_data
    weather_dict, icon = get_weather_data('KLAX')
    create_html_report(weather_dict, icon, "weather_page.html")

