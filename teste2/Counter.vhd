----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/27/2022 08:30:19 AM
-- Design Name: 
-- Module Name: Counter - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity Counter is
    generic(max : integer:=10);
    Port ( clk : in STD_LOGIC;
           reset : in STD_LOGIC;
           en : in STD_LOGIC;
           updown : in STD_LOGIC;
           number : out integer);
end Counter;

architecture Behavioral of Counter is

signal scnt:integer range 0 to max;

begin
process(clk,reset,en,updown)
        begin
            if reset='1' then
                scnt <= 0;
            elsif rising_edge(clk) then
                if en = '1' then
                
                    if  scnt<max and scnt>-max then
                        if updown='0' then
                            scnt <= scnt+1;
                        else
                            scnt <= scnt-1;
                        end if;
                        
                    else
                        scnt<=0; 
                    end if;
            
                    
                 end if;
                    
                    
                end if;

        end process;
number<=scnt;

end Behavioral;
