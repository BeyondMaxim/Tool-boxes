
namespace NinjaTrader.NinjaScript.Strategies
{
    public class MyCustomStrategy25 : Strategy
    {
        private double triggerPrice;
        private bool isPositionOpened;

        protected override void OnStateChange()
        {
            if (State == State.SetDefaults)
            {
                Description = "Detect Multiple of 25 Crossover";
                Name = "MyCustomStrategy25";
                Calculate = Calculate.OnBarClose;
                EntriesPerDirection = 1;
                EntryHandling = EntryHandling.AllEntries;
                IsExitOnSessionCloseStrategy = true;
                ExitOnSessionCloseSeconds = 30;
            }
            else if (State == State.Historical)
            {
                isPositionOpened = false; // Reset position state in historical mode
            }
        }

        protected override void OnBarUpdate()
        {
            // Determine if multiple of 25 is crossed
			Print("Now, Close value is " + Close[0]);
            if (Close[0] * 100 % 25 == 0)
            {
                triggerPrice = Close[0];
				Print("Now, TriggerPrice is " + Close[0]);
            }

            // Validate trade after waiting for 3 points
            if (triggerPrice != 0 && Math.Abs(Close[0] - triggerPrice) >= 3)
            {
                // Fire Buy or Sell signal only if position is not already opened
                if (!isPositionOpened)
                {
                    if (Close[0] > triggerPrice)
                    {
                        EnterLong();
                        isPositionOpened = true; // Set position state to opened
                    }
                    
                }
                else 
                {
                    if (Close[0] < triggerPrice)
                    {
                        EnterShort();
                        isPositionOpened = false; // Set position state to opened
                    }
                }
                triggerPrice = 0; // Reset trigger price
            }
        }
		
	
	    
		
		protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
	    {
	        if (order.OrderState == OrderState.Filled)
	        {
	            if (order.OrderAction == OrderAction.Buy)
	            {
	                // Buy order filled
	                Print("Buy order filled with fill price: " + order.AverageFillPrice);
	                // Do additional processing or logic here
	            }
	            else if (order.OrderAction == OrderAction.Sell)
	            {
	                // Sell order filled
	                Print("Sell order filled with fill price: " + order.AverageFillPrice);
	                // Do additional processing or logic here
	            }
	        }
	        else if (order.OrderState == OrderState.Cancelled || order.OrderState == OrderState.Rejected)
	        {
	            // Handle cancelled or rejected order
	            Print("Order cancelled or rejected: " + order.ToString());
	            
	        }
	    }
    }

}