from datetime import datetime


class Reservation:
    def __init__(self, client, service, duration):
        try:
            self.client = client
            self.service = service
            self.duration = duration
            self.status = "Pending"
            self.total_cost = 0

            self.validate_reservation()
            self.write_log("Reservation created successfully.")

        except Exception as error:
            self.write_log("Error creating reservation: " + str(error))
            raise ReservationError("The reservation could not be created.") from error

        finally:
            print("Reservation creation process finished.")

    def validate_reservation(self):
        try:
            if self.client is None:
                raise ReservationError("Client is required.")

            if self.service is None:
                raise ReservationError("Service is required.")

            if self.duration is None:
                raise ReservationError("Duration is required.")

            if not isinstance(self.duration, (int, float)):
                raise ReservationError("Duration must be a number.")

            if self.duration <= 0:
                raise ReservationError("Duration must be greater than zero.")

            if self.status not in ["Pending", "Confirmed", "Cancelled", "Processed"]:
                raise ReservationError("Invalid reservation status.")

        except ReservationError as error:
            self.write_log("Validation error: " + str(error))
            raise

    def confirm_reservation(self):
        try:
            if self.status == "Cancelled":
                raise ReservationError("A cancelled reservation cannot be confirmed.")

            if self.status == "Processed":
                raise ReservationError("A processed reservation cannot be confirmed again.")

            if self.status == "Confirmed":
                raise ReservationError("The reservation is already confirmed.")

        except ReservationError as error:
            self.write_log("Error confirming reservation: " + str(error))
            print("Error:", error)

        else:
            self.status = "Confirmed"
            self.write_log("Reservation confirmed.")
            print("Reservation confirmed successfully.")

        finally:
            print("Confirmation process finished.")

    def cancel_reservation(self):
        try:
            if self.status == "Processed":
                raise ReservationError("A processed reservation cannot be cancelled.")

            if self.status == "Cancelled":
                raise ReservationError("The reservation is already cancelled.")

        except ReservationError as error:
            self.write_log("Error cancelling reservation: " + str(error))
            print("Error:", error)

        else:
            self.status = "Cancelled"
            self.write_log("Reservation cancelled.")
            print("Reservation cancelled successfully.")

        finally:
            print("Cancellation process finished.")

    def process_reservation(self):
        try:
            if self.status != "Confirmed":
                raise ReservationError("Only confirmed reservations can be processed.")

            try:
                self.total_cost = self.service.calculate_cost(self.duration)

            except Exception as error:
                self.write_log("Cost calculation error: " + str(error))
                raise ReservationError("There was a problem calculating the reservation cost.") from error

            if self.total_cost <= 0:
                raise ReservationError("The total cost is not valid.")

        except ReservationError as error:
            self.write_log("Error processing reservation: " + str(error))
            print("Error:", error)

        else:
            self.status = "Processed"
            self.write_log("Reservation processed. Total cost: " + str(self.total_cost))
            print("Reservation processed successfully.")
            print("Total cost:", self.total_cost)

        finally:
            print("Processing reservation finished.")

    def show_reservation(self):
        print("\n--- Reservation Information ---")
        print("Client:", self.client)
        print("Service:", self.service)
        print("Duration:", self.duration)
        print("Status:", self.status)
        print("Total cost:", self.total_cost)

    def write_log(self, message):
        with open("system_logs.txt", "a", encoding="utf-8") as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(date + " - " + message + "\n")