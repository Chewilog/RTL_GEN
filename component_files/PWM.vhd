----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 26.06.2022 16:42:28
-- Design Name: 
-- Module Name: PWM - Behavioral
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
use IEEE.STD_LOGIC_unsigned.ALL;
use IEEE.NUMERIC_STD.ALL;


-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity PWM is
    generic( dutyCicle: std_logic := '0');
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pwm : out STD_LOGIC);
end PWM;

architecture Behavioral of PWM is

signal clk_aux: std_logic:='1';
signal cnt : integer range 0 to 1250000 := 0;
signal preset : integer;
constant full_cicle : integer := 1250000;


begin

pwm<=clk_aux;

preset <= 375000 when dutyCicle = '0' else
          625000 when dutyCicle = '1' else
          0;

    process(clk,rst)  --Possivel fonte de problema pelo else
    begin
        if rst='1' then
            cnt <= 0;
            clk_aux <= '0';
        elsif rising_edge(clk) then 
            if cnt<=preset then
                clk_aux <= '1';
                cnt <= cnt + 1;
            else 
                clk_aux <= '0';
                if cnt = full_cicle then 
                    cnt<=0;
                else
                    cnt <= cnt + 1;
                end if;     
            end if;            
            
            
        end if;
    end process;
    
end Behavioral;
