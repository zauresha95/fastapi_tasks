from datetime import date
from sqlalchemy import Column, Computed, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base

#
# class Tasks(Base):
    # __allow_unmapped__ = True
    # __tablename__ = "tasks"

    # task_id: Column(Integer, primary_key=True, autoincrement=True)
    # category: Column(String, nullable=False)
    # name: Column(String, nullable=False)
    # time_to_do: Column(String, nullable=False)
    # priority: Column(String, nullable=False)
    # repeat: Column(String, nullable=False)


class Tasks(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    # room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) \
    category: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    time_to_do: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    repeat: Mapped[str] = mapped_column(String)
    # date_to: Mapped[date] = mapped_column(Date)
    # price: Mapped[int]
    # total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    # total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))
    #
    # user: Mapped["Users"] = relationship(back_populates="bookings")
    #room: Mapped["Rooms"] = relationship(back_populates="bookings")

    def __str__(self):
        return f"Booking #{self.task_id}"
#
#
# class Tasks(Base):
#     __tablename__ = "tasks"
#
#     task_id: Mapped[int] = mapped_column(primary_key=True)
#     status: Mapped[str] = mapped_column(String)
#     name: Mapped[str] = mapped_column(String)
#
#     def __str__(self):
#         return f"Booking #{self.task_id}"