----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/30/2022 10:25:32 PM
-- Design Name: 
-- Module Name: reg8 - Behavioral
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

entity reg8 is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           clr : in STD_LOGIC;
           ld : in STD_LOGIC;
           X : in STD_LOGIC_VECTOR(7 DOWNTO 0);
           Y : out STD_LOGIC_VECTOR(7 DOWNTO 0));
end reg8;

architecture Behavioral of reg8 is

begin


process(clk, rst,clr,X)
begin 

    if rst='1' then
        Y<=(others=>'0');
    elsif rising_edge(clk) then
        if clr='1' then 
            Y<=(others=>'0');
        elsif ld='1' then
            Y<=X;
        end if;
    end if;


end process;




end Behavioral;
