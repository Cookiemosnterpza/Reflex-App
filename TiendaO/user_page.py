import reflex as rx
from .Models.Tabla_usarios import User
from .Services.User_service import select_all


class UserState(rx.State):
    #states
    users:list[User]

    @rx.event(background=True)
    async def get_all_user(self):
        async with self:
            self.users = select_all()


@rx.page(route="/user", title="user", on_load=UserState.get_all_user)
def user_pages() -> rx.Component:
    return rx.flex(
        rx.heading("usuarios", align="center"),
       

        table_user(UserState.users),
        direction="column",
        style={"width":"60vw", "margin":"auto"}
    )



def table_user(list_user: list[User]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.column_header_cell("Nombre"),
            rx.table.column_header_cell("Email"),
            rx.table.column_header_cell("Contraseña"),
            rx.table.column_header_cell("Tipo"),
            #rx.table.column_header_cell("Fecha creacion"),
        ),
        rx.table.body(
            rx.foreach(list_user, row_table)
        )
    )


def row_table(user:User) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.Nombre),
        rx.table.cell(user.Email),
        rx.table.cell(user.Contraseña),
        rx.table.cell(user.tipo),
        #rx.table.cell(user.fecha_creacion),
        rx.table.cell(rx.hstack(
            rx.button("Eliminar")
        ))
    )