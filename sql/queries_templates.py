quotes = {
    "ROUTE_SUM": {
        'sql_template': ("SELECT  ROUTE_NAME, ON_DATE, DEPART_ID, ARRIVE_ID, SUM(VALUE) AS SUM_VALUES "
                         "FROM FUZZY_SEARCH.PASSENGERS_FLOW_DATA "
                         "WHERE ROUTE_NAME = '{route_name}' "
                         "GROUP BY ROUTE_NAME, DEPART_ID, ARRIVE_ID, ON_DATE"),
        'params': {
            'route_name': None
        }
    },
    "ROUTE_NAMES": {
        'sql_template': ("SELECT ROUTE_NAME "
                         "FROM FUZZY_SEARCH.PASSENGERS_FLOW_DATA "
                         "GROUP BY ROUTE_NAME"),
        'params': None
    },
    "ROUTE_SUM_DAY_OF_YEAR": {
        'sql_template': ("SELECT  ROUTE_NAME, TO_CHAR(ON_DATE, 'DDD') AS ON_DAY, DEPART_ID, ARRIVE_ID, SUM(VALUE) AS SUM_VALUES "
                         "FROM FUZZY_SEARCH.PASSENGERS_FLOW_DATA "
                         "WHERE ROUTE_NAME = '{route_name}' "
                         "GROUP BY ROUTE_NAME, DEPART_ID, ARRIVE_ID, ON_DATE"),
        'params': {
            'route_name': None
        }
    }
}
