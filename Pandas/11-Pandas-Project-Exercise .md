<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Pandas-Project-Exercise" data-toc-modified-id="Pandas-Project-Exercise-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Pandas Project Exercise</a></span></li><li><span><a href="#The-Data" data-toc-modified-id="The-Data-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>The Data</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#NOTE:" data-toc-modified-id="NOTE:-2.0.0.1"><span class="toc-item-num">2.0.0.1&nbsp;&nbsp;</span>NOTE:</a></span></li></ul></li></ul></li><li><span><a href="#Data-Column-Reference" data-toc-modified-id="Data-Column-Reference-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span><div style="text-align: center">Data Column Reference</div></a></span></li></ul></li><li><span><a href="#TASKS" data-toc-modified-id="TASKS-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>TASKS</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#TASK:-Run-the-following-code-to-read-in-the-&quot;hotel_booking_data.csv&quot;-file.-Feel-free-to-explore-the-file-a-bit-before-continuing-with-the-rest-of-the-exercise." data-toc-modified-id="TASK:-Run-the-following-code-to-read-in-the-&quot;hotel_booking_data.csv&quot;-file.-Feel-free-to-explore-the-file-a-bit-before-continuing-with-the-rest-of-the-exercise.-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>TASK: Run the following code to read in the "hotel_booking_data.csv" file. Feel free to explore the file a bit before continuing with the rest of the exercise.</a></span><ul class="toc-item"><li><span><a href="#TASK:-How-many-rows-are-there?" data-toc-modified-id="TASK:-How-many-rows-are-there?-3.0.1.1"><span class="toc-item-num">3.0.1.1&nbsp;&nbsp;</span><strong>TASK: How many rows are there?</strong></a></span></li><li><span><a href="#TASK:-Is-there-any-missing-data?-If-so,-which-column-has-the-most-missing-data?" data-toc-modified-id="TASK:-Is-there-any-missing-data?-If-so,-which-column-has-the-most-missing-data?-3.0.1.2"><span class="toc-item-num">3.0.1.2&nbsp;&nbsp;</span><strong>TASK: Is there any missing data? If so, which column has the most missing data?</strong></a></span></li><li><span><a href="#TASK:-Drop-the-&quot;company&quot;-column-from-the-dataset." data-toc-modified-id="TASK:-Drop-the-&quot;company&quot;-column-from-the-dataset.-3.0.1.3"><span class="toc-item-num">3.0.1.3&nbsp;&nbsp;</span><strong>TASK: Drop the "company" column from the dataset.</strong></a></span></li><li><span><a href="#TASK:-What-are-the-top-5-most-common-country-codes-in-the-dataset?" data-toc-modified-id="TASK:-What-are-the-top-5-most-common-country-codes-in-the-dataset?-3.0.1.4"><span class="toc-item-num">3.0.1.4&nbsp;&nbsp;</span><strong>TASK: What are the top 5 most common country codes in the dataset?</strong></a></span></li><li><span><a href="#TASK:-What-is-the-name-of-the-person-who-paid-the-highest-ADR-(average-daily-rate)?-How-much-was-their-ADR?" data-toc-modified-id="TASK:-What-is-the-name-of-the-person-who-paid-the-highest-ADR-(average-daily-rate)?-How-much-was-their-ADR?-3.0.1.5"><span class="toc-item-num">3.0.1.5&nbsp;&nbsp;</span><strong>TASK: What is the name of the person who paid the highest ADR (average daily rate)? How much was their ADR?</strong></a></span></li><li><span><a href="#TASK:-The-adr-is-the-average-daily-rate-for-a-person's-stay-at-the-hotel.-What-is-the-mean-adr-across-all-the-hotel-stays-in-the-dataset?" data-toc-modified-id="TASK:-The-adr-is-the-average-daily-rate-for-a-person's-stay-at-the-hotel.-What-is-the-mean-adr-across-all-the-hotel-stays-in-the-dataset?-3.0.1.6"><span class="toc-item-num">3.0.1.6&nbsp;&nbsp;</span><strong>TASK: The adr is the average daily rate for a person's stay at the hotel. What is the mean adr across all the hotel stays in the dataset?</strong></a></span></li><li><span><a href="#TASK:-What-is-the-average-(mean)-number-of-nights-for-a-stay-across-the-entire-data-set?-Feel-free-to-round-this-to-2-decimal-points." data-toc-modified-id="TASK:-What-is-the-average-(mean)-number-of-nights-for-a-stay-across-the-entire-data-set?-Feel-free-to-round-this-to-2-decimal-points.-3.0.1.7"><span class="toc-item-num">3.0.1.7&nbsp;&nbsp;</span><strong>TASK: What is the average (mean) number of nights for a stay across the entire data set? Feel free to round this to 2 decimal points.</strong></a></span></li><li><span><a href="#TASK:-What-is-the-average-total-cost-for-a-stay-in-the-dataset?-Not-average-daily-cost,-but-total-stay-cost.-(You-will-need-to-calculate-total-cost-your-self-by-using-ADR-and-week-day-and-weeknight-stays).-Feel-free-to-round-this-to-2-decimal-points." data-toc-modified-id="TASK:-What-is-the-average-total-cost-for-a-stay-in-the-dataset?-Not-average-daily-cost,-but-total-stay-cost.-(You-will-need-to-calculate-total-cost-your-self-by-using-ADR-and-week-day-and-weeknight-stays).-Feel-free-to-round-this-to-2-decimal-points.-3.0.1.8"><span class="toc-item-num">3.0.1.8&nbsp;&nbsp;</span><strong>TASK: What is the average total cost for a stay in the dataset? Not <em>average daily cost</em>, but <em>total</em> stay cost. (You will need to calculate total cost your self by using ADR and week day and weeknight stays). Feel free to round this to 2 decimal points.</strong></a></span></li><li><span><a href="#TASK:-What-are-the-names-and-emails-of-people-who-made-exactly-5-&quot;Special-Requests&quot;?" data-toc-modified-id="TASK:-What-are-the-names-and-emails-of-people-who-made-exactly-5-&quot;Special-Requests&quot;?-3.0.1.9"><span class="toc-item-num">3.0.1.9&nbsp;&nbsp;</span><strong>TASK: What are the names and emails of people who made exactly 5 "Special Requests"?</strong></a></span></li><li><span><a href="#TASK:-What-are-the-top-5-most-common-last-name-in-the-dataset?-Bonus:-Can-you-figure-this-out-in-one-line-of-pandas-code?-(For-simplicity-treat-the-a-title-such-as-MD-as-a-last-name,-for-example-Caroline-Conley-MD-can-be-said-to-have-the-last-name-MD)" data-toc-modified-id="TASK:-What-are-the-top-5-most-common-last-name-in-the-dataset?-Bonus:-Can-you-figure-this-out-in-one-line-of-pandas-code?-(For-simplicity-treat-the-a-title-such-as-MD-as-a-last-name,-for-example-Caroline-Conley-MD-can-be-said-to-have-the-last-name-MD)-3.0.1.10"><span class="toc-item-num">3.0.1.10&nbsp;&nbsp;</span><strong>TASK: What are the top 5 most common last name in the dataset? Bonus: Can you figure this out in one line of pandas code? (For simplicity treat the a title such as MD as a last name, for example Caroline Conley MD can be said to have the last name MD)</strong></a></span></li><li><span><a href="#TASK:-What-are-the-names-of-the-people-who-had-booked-the-most-number-children-and-babies-for-their-stay?-(Don't-worry-if-they-canceled,-only-consider-number-of-people-reported-at-the-time-of-their-reservation)" data-toc-modified-id="TASK:-What-are-the-names-of-the-people-who-had-booked-the-most-number-children-and-babies-for-their-stay?-(Don't-worry-if-they-canceled,-only-consider-number-of-people-reported-at-the-time-of-their-reservation)-3.0.1.11"><span class="toc-item-num">3.0.1.11&nbsp;&nbsp;</span><strong>TASK: What are the names of the people who had booked the most number children and babies for their stay? (Don't worry if they canceled, only consider number of people reported at the time of their reservation)</strong></a></span></li><li><span><a href="#TASK:-What-are-the-top-3-most-common-area-code-in-the-phone-numbers?-(Area-code-is-first-3-digits)" data-toc-modified-id="TASK:-What-are-the-top-3-most-common-area-code-in-the-phone-numbers?-(Area-code-is-first-3-digits)-3.0.1.12"><span class="toc-item-num">3.0.1.12&nbsp;&nbsp;</span><strong>TASK: What are the top 3 most common area code in the phone numbers? (Area code is first 3 digits)</strong></a></span></li><li><span><a href="#TASK:-How-many-arrivals-took-place-between-the-1st-and-the-15th-of-the-month-(inclusive-of-1-and-15)-?-Bonus:-Can-you-do-this-in-one-line-of-pandas-code?" data-toc-modified-id="TASK:-How-many-arrivals-took-place-between-the-1st-and-the-15th-of-the-month-(inclusive-of-1-and-15)-?-Bonus:-Can-you-do-this-in-one-line-of-pandas-code?-3.0.1.13"><span class="toc-item-num">3.0.1.13&nbsp;&nbsp;</span><strong>TASK: How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15) ? Bonus: Can you do this in one line of pandas code?</strong></a></span></li><li><span><a href="#HARD-BONUS-TASK:-Create-a-table-for-counts-for-each-day-of-the-week-that-people-arrived.-(E.g.-5000-arrivals-were-on-a-Monday,-3000-were-on-a-Tuesday,-etc..)" data-toc-modified-id="HARD-BONUS-TASK:-Create-a-table-for-counts-for-each-day-of-the-week-that-people-arrived.-(E.g.-5000-arrivals-were-on-a-Monday,-3000-were-on-a-Tuesday,-etc..)-3.0.1.14"><span class="toc-item-num">3.0.1.14&nbsp;&nbsp;</span><strong>HARD BONUS TASK: Create a table for counts for each day of the week that people arrived. (E.g. 5000 arrivals were on a Monday, 3000 were on a Tuesday, etc..)</strong></a></span></li></ul></li></ul></li></ul></li></ul></div>

# Pandas Project Exercise 

# The Data

This data set contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things.

All personally identifying information has been removed from the data.

Acknowledgements
The data is originally from the article Hotel Booking Demand Datasets, written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.


----------------------------

#### NOTE:
**Names, Emails, Phone Numbers, and Credit Card numbers in the data are synthetic and not real information from people. The hotel data is real from the publication listed above.**

## <div style="text-align: center">Data Column Reference</div>

<table><thead><tr class="rowsep-1"><th scope="col"><strong>Variable</strong></th><th scope="col"><strong>Type</strong></th><th scope="col"><strong>Description</strong></th><th scope="col"><strong>Source/Engineering</strong></th></tr></thead><tbody><tr><th scope="row"><em>ADR</em></th><td>Numeric</td><td>Average Daily Rate as defined by <a name="bbib5" href="#bib5" class="workspace-trigger">[5]</a></td><td>BO, BL and TR / Calculated by dividing the sum of all lodging transactions by the total number of staying nights</td></tr><tr><th scope="row"><em>Adults</em></th><td>Integer</td><td>Number of adults</td><td>BO and BL</td></tr><tr><th scope="row"><em>Agent</em></th><td>Categorical</td><td>ID of the travel agency that made the booking<a name="btbl1fna" href="#tbl1fna" class="workspace-trigger"><sup>a</sup></a></td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateDayOfMonth</em></th><td>Integer</td><td>Day of the month of the arrival date</td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateMonth</em></th><td>Categorical</td><td>Month of arrival date with 12 categories: “January” to “December”</td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateWeekNumber</em></th><td>Integer</td><td>Week number of the arrival date</td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateYear</em></th><td>Integer</td><td>Year of arrival date</td><td>BO and BL</td></tr><tr><th scope="row"><em>AssignedRoomType</em></th><td>Categorical</td><td>Code for the type of room assigned to the booking. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g. overbooking) or by customer request. Code is presented instead of designation for anonymity reasons</td><td>BO and BL</td></tr><tr><th scope="row"><em>Babies</em></th><td>Integer</td><td>Number of babies</td><td>BO and BL</td></tr><tr><th scope="row"><em>BookingChanges</em></th><td>Integer</td><td>Number of changes/amendments made to the booking from the moment the booking was entered on the PMS until the moment of check-in or cancellation</td><td>BO and BL/Calculated by adding the number of unique iterations that change some of the booking attributes, namely: persons, arrival date, nights, reserved room type or meal</td></tr><tr><th scope="row"><em>Children</em></th><td>Integer</td><td>Number of children</td><td>BO and BL/Sum of both payable and non-payable children</td></tr><tr><th scope="row"><em>Company</em></th><td>Categorical</td><td>ID of the company/entity that made the booking or responsible for paying the booking. ID is presented instead of designation for anonymity reasons</td><td>BO and BL.</td></tr><tr><th scope="row"><em>Country</em></th><td>Categorical</td><td>Country of origin. Categories are represented in the ISO 3155–3:2013 format <a name="bbib6" href="#bib6" class="workspace-trigger">[6]</a></td><td>BO, BL and NT</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="5"><em>CustomerType</em></th><td rowspan="5">Categorical</td><td>Type of booking, assuming one of four categories:</td><td rowspan="5">BO and BL</td></tr><tr><td>Contract - when the booking has an allotment or other type of contract associated to it;</td></tr><tr><td>Group – when the booking is associated to a group;</td></tr><tr><td>Transient – when the booking is not part of a group or contract, and is not associated to other transient booking;</td></tr><tr><td>Transient-party – when the booking is transient, but is associated to at least other transient booking</td></tr><tr><th scope="row"><em>DaysInWaitingList</em></th><td>Integer</td><td>Number of days the booking was in the waiting list before it was confirmed to the customer</td><td>BO/Calculated by subtracting the date the booking was confirmed to the customer from the date the booking entered on the PMS</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="7"><em>DepositType</em></th><td rowspan="7">Categorical</td><td>Indication on if the customer made a deposit to guarantee the booking. This variable can assume three categories:</td><td rowspan="2">BO and TR/Value calculated based on the payments identified for the booking in the transaction (TR) table before the booking׳s arrival or cancellation date.</td></tr><tr><td rowspan="3">No Deposit – no deposit was made;</td></tr><tr><td>In case no payments were found the value is “No Deposit”.</td></tr><tr><td rowspan="2">If the payment was equal or exceeded the total cost of stay, the value is set as “Non Refund”.</td></tr><tr><td rowspan="2">Non Refund – a deposit was made in the value of the total stay cost;</td></tr><tr><td rowspan="2">Otherwise the value is set as “Refundable”</td></tr><tr><td>Refundable – a deposit was made with a value under the total cost of stay.</td></tr><tr><th scope="row"><em>DistributionChannel</em></th><td>Categorical</td><td>Booking distribution channel. The term “TA” means “Travel Agents” and “TO” means “Tour Operators”</td><td>BO, BL and DC</td></tr><tr><th scope="row"><em>IsCanceled</em></th><td>Categorical</td><td>Value indicating if the booking was canceled (1) or not (0)</td><td>BO</td></tr><tr><th scope="row"><em>IsRepeatedGuest</em></th><td>Categorical</td><td>Value indicating if the booking name was from a repeated guest (1) or not (0)</td><td>BO, BL and C/ Variable created by verifying if a profile was associated with the booking customer. If so, and if the customer profile creation date was prior to the creation date for the booking on the PMS database it was assumed the booking was from a repeated guest</td></tr><tr><th scope="row"><em>LeadTime</em></th><td>Integer</td><td>Number of days that elapsed between the entering date of the booking into the PMS and the arrival date</td><td>BO and BL/ Subtraction of the entering date from the arrival date</td></tr><tr><th scope="row"><em>MarketSegment</em></th><td>Categorical</td><td>Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”</td><td>BO, BL and MS</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="5"><em>Meal</em></th><td rowspan="5">Categorical</td><td>Type of meal booked. Categories are presented in standard hospitality meal packages:</td><td rowspan="5">BO, BL and ML</td></tr><tr><td>Undefined/SC – no meal package;</td></tr><tr><td>BB – Bed &amp; Breakfast;</td></tr><tr><td>HB – Half board (breakfast and one other meal – usually dinner);</td></tr><tr><td>FB – Full board (breakfast, lunch and dinner)</td></tr><tr><th scope="row"><em>PreviousBookingsNotCanceled</em></th><td>Integer</td><td>Number of previous bookings not cancelled by the customer prior to the current booking</td><td>BO and BL / In case there was no customer profile associated with the booking, the value is set to 0. Otherwise, the value is the number of bookings with the same customer profile created before the current booking and not canceled.</td></tr><tr><th scope="row"><em>PreviousCancellations</em></th><td>Integer</td><td>Number of previous bookings that were cancelled by the customer prior to the current booking</td><td>BO and BL/ In case there was no customer profile associated with the booking, the value is set to 0. Otherwise, the value is the number of bookings with the same customer profile created before the current booking and canceled.</td></tr><tr><th scope="row"><em>RequiredCardParkingSpaces</em></th><td>Integer</td><td>Number of car parking spaces required by the customer</td><td>BO and BL</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="4"><em>ReservationStatus</em></th><td rowspan="4">Categorical</td><td>Reservation last status, assuming one of three categories:</td><td rowspan="4">BO</td></tr><tr><td>Canceled – booking was canceled by the customer;</td></tr><tr><td>Check-Out – customer has checked in but already departed;</td></tr><tr><td>No-Show – customer did not check-in and did inform the hotel of the reason why</td></tr><tr><th scope="row"><em>ReservationStatusDate</em></th><td>Date</td><td>Date at which the last status was set. This variable can be used in conjunction with the <em>ReservationStatus</em> to understand when was the booking canceled or when did the customer checked-out of the hotel</td><td>BO</td></tr><tr><th scope="row"><em>ReservedRoomType</em></th><td>Categorical</td><td>Code of room type reserved. Code is presented instead of designation for anonymity reasons</td><td>BO and BL</td></tr><tr><th scope="row"><em>StaysInWeekendNights</em></th><td>Integer</td><td>Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel</td><td>BO and BL/ Calculated by counting the number of weekend nights from the total number of nights</td></tr><tr><th scope="row"><em>StaysInWeekNights</em></th><td>Integer</td><td>Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel</td><td>BO and BL/Calculated by counting the number of week nights from the total number of nights</td></tr><tr><th scope="row"><em>TotalOfSpecialRequests</em></th><td>Integer</td><td>Number of special requests made by the customer (e.g. twin bed or high floor)</td><td>BO and BL/Sum of all special requests</td></tr></tbody></table>

-----------

# TASKS

**Complete the tasks shown in bold below. The expected output is shown in a cell below. Be careful not to run the cell above the expected output, as it will clear the expected output. Try your best to solve these in one line of pandas code (not every single question can be solved in one line, but many can be!) Refer to solutions notebook and video to view possible solutions. NOTE: Many tasks have multiple correct solution methods!**

-----
### TASK: Run the following code to read in the "hotel_booking_data.csv" file. Feel free to explore the file a bit before continuing with the rest of the exercise.


```python
import pandas as pd
```


```python
hotels = pd.read_csv("hotel_booking_data.csv")
```


```python
hotels.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hotel</th>
      <th>is_canceled</th>
      <th>lead_time</th>
      <th>arrival_date_year</th>
      <th>arrival_date_month</th>
      <th>arrival_date_week_number</th>
      <th>arrival_date_day_of_month</th>
      <th>stays_in_weekend_nights</th>
      <th>stays_in_week_nights</th>
      <th>adults</th>
      <th>...</th>
      <th>customer_type</th>
      <th>adr</th>
      <th>required_car_parking_spaces</th>
      <th>total_of_special_requests</th>
      <th>reservation_status</th>
      <th>reservation_status_date</th>
      <th>name</th>
      <th>email</th>
      <th>phone-number</th>
      <th>credit_card</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>342</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>Transient</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>Check-Out</td>
      <td>2015-07-01</td>
      <td>Ernest Barnes</td>
      <td>Ernest.Barnes31@outlook.com</td>
      <td>669-792-1661</td>
      <td>************4322</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>737</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>Transient</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>Check-Out</td>
      <td>2015-07-01</td>
      <td>Andrea Baker</td>
      <td>Andrea_Baker94@aol.com</td>
      <td>858-637-6955</td>
      <td>************9157</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>7</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Transient</td>
      <td>75.0</td>
      <td>0</td>
      <td>0</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
      <td>Rebecca Parker</td>
      <td>Rebecca_Parker@comcast.net</td>
      <td>652-885-2745</td>
      <td>************3734</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>13</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Transient</td>
      <td>75.0</td>
      <td>0</td>
      <td>0</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
      <td>Laura Murray</td>
      <td>Laura_M@gmail.com</td>
      <td>364-656-8427</td>
      <td>************5677</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>14</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>Transient</td>
      <td>98.0</td>
      <td>0</td>
      <td>1</td>
      <td>Check-Out</td>
      <td>2015-07-03</td>
      <td>Linda Hines</td>
      <td>LHines@verizon.com</td>
      <td>713-226-5883</td>
      <td>************5498</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 36 columns</p>
</div>



---
#### **TASK: How many rows are there?**


```python
# CODE HERE
```


```python

```




    119390



#### **TASK: Is there any missing data? If so, which column has the most missing data?**


```python
# CODE HERE
```


```python

```




    hotel                                  0
    is_canceled                            0
    lead_time                              0
    arrival_date_year                      0
    arrival_date_month                     0
    arrival_date_week_number               0
    arrival_date_day_of_month              0
    stays_in_weekend_nights                0
    stays_in_week_nights                   0
    adults                                 0
    children                               4
    babies                                 0
    meal                                   0
    country                              488
    market_segment                         0
    distribution_channel                   0
    is_repeated_guest                      0
    previous_cancellations                 0
    previous_bookings_not_canceled         0
    reserved_room_type                     0
    assigned_room_type                     0
    booking_changes                        0
    deposit_type                           0
    agent                              16340
    company                           112593
    days_in_waiting_list                   0
    customer_type                          0
    adr                                    0
    required_car_parking_spaces            0
    total_of_special_requests              0
    reservation_status                     0
    reservation_status_date                0
    name                                   0
    email                                  0
    phone-number                           0
    credit_card                            0
    dtype: int64




```python

```

    Yes, missing data, company column missing: 112593 rows.
    

#### **TASK: Drop the "company" column from the dataset.**


```python
# CODE HERE
```


```python

```

#### **TASK: What are the top 5 most common country codes in the dataset?**


```python
# CODE HERE
```


```python

```




    PRT    48590
    GBR    12129
    FRA    10415
    ESP     8568
    DEU     7287
    Name: country, dtype: int64



#### **TASK: What is the name of the person who paid the highest ADR (average daily rate)? How much was their ADR?**


```python
# CODE HERE
```


```python

```




    adr              5400
    name    Daniel Walter
    Name: 48515, dtype: object



#### **TASK: The adr is the average daily rate for a person's stay at the hotel. What is the mean adr across all the hotel stays in the dataset?**


```python
# CODE HERE
```


```python

```




    101.83



#### **TASK: What is the average (mean) number of nights for a stay across the entire data set? Feel free to round this to 2 decimal points.**


```python
# CODE HERE
```


```python

```




    3.43



#### **TASK: What is the average total cost for a stay in the dataset? Not *average daily cost*, but *total* stay cost. (You will need to calculate total cost your self by using ADR and week day and weeknight stays). Feel free to round this to 2 decimal points.**


```python
# CODE HERE
```


```python

```




    357.85



#### **TASK: What are the names and emails of people who made exactly 5 "Special Requests"?**


```python
# CODE HERE
```


```python

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7860</th>
      <td>Amanda Harper</td>
      <td>Amanda.H66@yahoo.com</td>
    </tr>
    <tr>
      <th>11125</th>
      <td>Laura Sanders</td>
      <td>Sanders_Laura@hotmail.com</td>
    </tr>
    <tr>
      <th>14596</th>
      <td>Tommy Ortiz</td>
      <td>Tommy_O@hotmail.com</td>
    </tr>
    <tr>
      <th>14921</th>
      <td>Gilbert Miller</td>
      <td>Miller.Gilbert@aol.com</td>
    </tr>
    <tr>
      <th>14922</th>
      <td>Timothy Torres</td>
      <td>TTorres@protonmail.com</td>
    </tr>
    <tr>
      <th>24630</th>
      <td>Jennifer Weaver</td>
      <td>Jennifer_W@aol.com</td>
    </tr>
    <tr>
      <th>27288</th>
      <td>Crystal Horton</td>
      <td>Crystal.H@mail.com</td>
    </tr>
    <tr>
      <th>27477</th>
      <td>Brittney Burke</td>
      <td>Burke_Brittney16@att.com</td>
    </tr>
    <tr>
      <th>29906</th>
      <td>Cynthia Cabrera</td>
      <td>Cabrera.Cynthia@xfinity.com</td>
    </tr>
    <tr>
      <th>29949</th>
      <td>Sarah Floyd</td>
      <td>Sarah_F@gmail.com</td>
    </tr>
    <tr>
      <th>32267</th>
      <td>Michelle Villa</td>
      <td>Michelle.Villa@aol.com</td>
    </tr>
    <tr>
      <th>39027</th>
      <td>Nichole Hebert</td>
      <td>Hebert.Nichole@gmail.com</td>
    </tr>
    <tr>
      <th>39129</th>
      <td>Lindsey Mckenzie</td>
      <td>Lindsey.Mckenzie@att.com</td>
    </tr>
    <tr>
      <th>39525</th>
      <td>Ashley Edwards</td>
      <td>Edwards.Ashley@yahoo.com</td>
    </tr>
    <tr>
      <th>70114</th>
      <td>Christopher Torres</td>
      <td>Torres.Christopher@gmail.com</td>
    </tr>
    <tr>
      <th>78819</th>
      <td>Mrs. Tara Sullivan DVM</td>
      <td>Mrs..DVM@xfinity.com</td>
    </tr>
    <tr>
      <th>78820</th>
      <td>Michaela Brown</td>
      <td>MichaelaBrown@att.com</td>
    </tr>
    <tr>
      <th>78822</th>
      <td>Kurt Maldonado MD</td>
      <td>KMD15@xfinity.com</td>
    </tr>
    <tr>
      <th>97072</th>
      <td>Jason Richardson</td>
      <td>Jason.R@zoho.com</td>
    </tr>
    <tr>
      <th>97099</th>
      <td>Terri Hurley</td>
      <td>THurley@xfinity.com</td>
    </tr>
    <tr>
      <th>97261</th>
      <td>Mrs. Caitlin Webb</td>
      <td>Mrs._W@comcast.net</td>
    </tr>
    <tr>
      <th>98410</th>
      <td>Holly Arroyo</td>
      <td>Arroyo_Holly@mail.com</td>
    </tr>
    <tr>
      <th>98674</th>
      <td>Denise Campbell</td>
      <td>Denise_C@gmail.com</td>
    </tr>
    <tr>
      <th>99887</th>
      <td>Michael Smith</td>
      <td>Michael.S42@aol.com</td>
    </tr>
    <tr>
      <th>99888</th>
      <td>Dr. Trevor Sellers</td>
      <td>Dr._S@aol.com</td>
    </tr>
    <tr>
      <th>101569</th>
      <td>Kayla Murphy</td>
      <td>Kayla.Murphy@yahoo.com</td>
    </tr>
    <tr>
      <th>102061</th>
      <td>Taylor Martinez</td>
      <td>Taylor.Martinez@hotmail.com</td>
    </tr>
    <tr>
      <th>109511</th>
      <td>Charles Wilson</td>
      <td>Charles_Wilson@yahoo.com</td>
    </tr>
    <tr>
      <th>109590</th>
      <td>Tyler Allison</td>
      <td>Tyler.A@protonmail.com</td>
    </tr>
    <tr>
      <th>110082</th>
      <td>Matthew Bailey</td>
      <td>Matthew_Bailey@aol.com</td>
    </tr>
    <tr>
      <th>110083</th>
      <td>Charlotte Acevedo</td>
      <td>Charlotte_A@verizon.com</td>
    </tr>
    <tr>
      <th>111909</th>
      <td>Darrell Brennan</td>
      <td>Brennan_Darrell51@hotmail.com</td>
    </tr>
    <tr>
      <th>111911</th>
      <td>Melinda Jensen</td>
      <td>MelindaJensen@zoho.com</td>
    </tr>
    <tr>
      <th>113915</th>
      <td>Terry Arnold</td>
      <td>Arnold.Terry@zoho.com</td>
    </tr>
    <tr>
      <th>114770</th>
      <td>Mary Nguyen</td>
      <td>Nguyen.Mary@protonmail.com</td>
    </tr>
    <tr>
      <th>114909</th>
      <td>Lindsay Cuevas</td>
      <td>Lindsay.Cuevas40@mail.com</td>
    </tr>
    <tr>
      <th>116455</th>
      <td>Cynthia Hernandez</td>
      <td>CynthiaHernandez@xfinity.com</td>
    </tr>
    <tr>
      <th>116457</th>
      <td>Angela Hawkins</td>
      <td>Angela_H@gmail.com</td>
    </tr>
    <tr>
      <th>118817</th>
      <td>Sue Lawson</td>
      <td>Sue.L52@comcast.net</td>
    </tr>
    <tr>
      <th>119161</th>
      <td>Alyssa Richards</td>
      <td>Alyssa_Richards@aol.com</td>
    </tr>
  </tbody>
</table>
</div>



**TASK: What percentage of hotel stays were classified as "repeat guests"? (Do not base this off the name of the person, but instead of the is_repeated_guest column)**


```python
#CODE HERE
```


```python

```




    3.19



#### **TASK: What are the top 5 most common last name in the dataset? Bonus: Can you figure this out in one line of pandas code? (For simplicity treat the a title such as MD as a last name, for example Caroline Conley MD can be said to have the last name MD)**


```python
#CODE HERE
```


```python

```




    Smith       2510
    Johnson     1998
    Williams    1628
    Jones       1441
    Brown       1433
    Name: name, dtype: int64



#### **TASK: What are the names of the people who had booked the most number children and babies for their stay? (Don't worry if they canceled, only consider number of people reported at the time of their reservation)**


```python
#CODE HERE
```


```python

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>adults</th>
      <th>total_kids</th>
      <th>babies</th>
      <th>children</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>328</th>
      <td>Jamie Ramirez</td>
      <td>2</td>
      <td>10.0</td>
      <td>0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>46619</th>
      <td>Nicholas Parker</td>
      <td>2</td>
      <td>10.0</td>
      <td>10</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>78656</th>
      <td>Marc Robinson</td>
      <td>1</td>
      <td>9.0</td>
      <td>9</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



#### **TASK: What are the top 3 most common area code in the phone numbers? (Area code is first 3 digits)**


```python
#CODE HERE
```


```python

```

    Code - Total Count
    




    799    168
    185    167
    541    166
    Name: phone-number, dtype: int64



#### **TASK: How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15) ? Bonus: Can you do this in one line of pandas code?**


```python
#CODE HERE
```


```python

```




    58152




#### **HARD BONUS TASK: Create a table for counts for each day of the week that people arrived. (E.g. 5000 arrivals were on a Monday, 3000 were on a Tuesday, etc..)**


```python
# CODE HERE
```


```python

```




    Friday       19631
    Thursday     19254
    Monday       18171
    Saturday     18055
    Wednesday    16139
    Sunday       14141
    Tuesday      13999
    Name: date, dtype: int64



---

---
