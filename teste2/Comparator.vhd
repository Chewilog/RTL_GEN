----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/27/2022 10:19:16 AM
-- Design Name: 
-- Module Name: Comparator - Behavioral
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

entity Comparator is
    Port ( a : in integer;
           b : in integer;
           op : in STD_LOGIC_VECTOR(2 downto 0);
           cmpout : out STD_LOGIC);
end Comparator;

architecture Behavioral of Comparator is

begin


process(a,b,op)
begin
    case op is
        when "000"  =>
            if a>=b then
                cmpout<='1';
            else
                cmpout<='0';
            end if;
            
        when "001"  =>
                if a<=b then
                    cmpout<='1';
                else
                    cmpout<='0';
                end if;
                
        when "010"  =>
            if a<b then
                cmpout<='1';
            else
                cmpout<='0';
            end if;
            
        when "011"  =>
            if a>b then
                cmpout<='1';
            else
                cmpout<='0';
            end if;
            
        when "100"  =>
            if a=b  then
                cmpout<='1';
            else
                cmpout<='0';
            end if;
            
        when "101"  =>
            if a/=b then
                cmpout<='1';
            else
                cmpout<='0';
            end if;
            
        when others =>
            cmpout<='0';
    end case;
end process;


    
    
    
end Behavioral;
