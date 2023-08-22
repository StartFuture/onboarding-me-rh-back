
from app.dao.dao import connect_database
from app.schemas.welcome_kit_wk_item import WelcomeKit_WKItem

def createWelcomeKit_WKItem(welcome_kit_wkitem: WelcomeKit_WKItem):

    connection, cursor = connect_database()

    query = f""" INSERT into WelcomeKit_WelcomeKitItem(welcome_kit_id, item_id)
    VALUES ("{welcome_kit_wkitem.welcome_kit_id}",
    "{welcome_kit_wkitem.item_id}"
    )
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit_wkitem

