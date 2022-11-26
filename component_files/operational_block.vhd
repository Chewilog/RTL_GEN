----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 02.07.2022 12:20:40
-- Design Name: 
-- Module Name: operational_block - Behavioral
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
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values


-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity operational_block is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           number : in std_logic_vector(7 downto 0);
           l_buffer : in STD_LOGIC;
           c_buffer : in STD_LOGIC;
           l_x : in STD_LOGIC;
           c_x : in STD_LOGIC;
           l_cnt : in STD_LOGIC;
           c_cnt : in STD_LOGIC;
           l_mean_add : in STD_LOGIC;
           c_mean_add : in STD_LOGIC;
           l_mean_div8 : in STD_LOGIC;
           c_mean_div8 : in STD_LOGIC;
           l_sub : in STD_LOGIC;
           c_sub : in STD_LOGIC;
           l_mul : in STD_LOGIC;
           c_mul : in STD_LOGIC;
           l_add : in STD_LOGIC;
           c_add : in STD_LOGIC;
           l_div8 : in STD_LOGIC;
           c_div8 : in STD_LOGIC;
           lt8 : out STD_LOGIC;
           result : out STD_LOGIC_VECTOR(15 downto 0));
           
end operational_block;

architecture Behavioral of operational_block is

component input_buffer_reg is
    Port ( clk : in STD_LOGIC;
           rst: in STD_LOGIC;
           x : in STD_LOGIC_VECTOR (7 downto 0);
           l_buffer : in STD_LOGIC;
           c_buffer : in STD_LOGIC;
           reg_output : out STD_LOGIC_VECTOR (7 downto 0));
end component;



type reg_output_array is array (0 to 7) of std_logic_vector(7 downto 0);


signal aux_reg_output : reg_output_array;

signal cnt_lt_8 : std_logic;
signal cnt : std_logic_vector(3 downto 0);
signal mean, sub_result : std_logic_vector(7 downto 0);
signal reg_out_mean_add : std_logic_vector(10 downto 0);
signal mult_result, sresult : std_logic_vector(15 downto 0);
signal reg_out_add19b : std_logic_vector(18 downto 0);





begin

reg1_8b:input_buffer_reg port map(          clk        =>clk,
                                            rst        =>rst,
                                            x          =>number,
                                            l_buffer   =>l_x,
                                            c_buffer   =>c_x,
                                            reg_output =>aux_reg_output(0));
PIPO: 
    for I in 1 to 7 generate
        regx_8b:input_buffer_reg port map(  clk        =>clk,
                                            rst        =>rst,
                                            x          =>aux_reg_output(I-1),
                                            l_buffer   =>l_buffer,
                                            c_buffer   =>c_buffer,
                                            reg_output =>aux_reg_output(I));
    end generate;
    
counter:process(clk,rst,c_cnt,l_cnt)
        begin
            if c_cnt='1' or rst='1' then
                cnt <= (others=>'0');
            elsif rising_edge(clk) then
                if l_cnt = '1' then
                    cnt <= std_logic_vector(unsigned(cnt) + 1);
                end if;
            end if;
        end process;
        
cnt_out:process(cnt,rst)
            begin
                if rst='1' then
                    cnt_lt_8 <= '0';
                elsif cnt < "1000" then
                    cnt_lt_8 <= '1';
                else
                    cnt_lt_8 <= '0';
                end if;
            end process;
            
mean_add_8b:process(clk,rst,c_mean_add,l_mean_add)
            begin
                if c_mean_add='1' or rst='1' then
                    reg_out_mean_add <= (others=>'0');
                elsif rising_edge(clk) then
                    if l_mean_add = '1' then
                        reg_out_mean_add <= std_logic_vector(signed(aux_reg_output(0)) + signed(reg_out_mean_add));
                    end if; 
                end if;
            end process;

mean_div8:process(clk,rst,c_mean_div8,l_mean_div8)
            begin
                if c_mean_div8='1' or rst='1' then
                    mean <= (others=>'0');
                elsif rising_edge(clk) then
                    if l_mean_div8 = '1' then
                        --regM <= shift_right(regS,3);
                        mean <= reg_out_mean_add(10 downto 3);
                    end if;
                end if;
            end process;

sub_8b:process(clk,rst,c_sub,l_sub)
        begin
            if c_sub='1' or rst='1' then
                sub_result <= (others=>'0');
            elsif rising_edge(clk) then
                if l_sub = '1' then
                    sub_result <= std_logic_vector(signed(aux_reg_output(7)) - signed(mean));
                end if; 
            end if;
        end process;


mult_8b_16b:process(clk,rst,c_mul,l_mul)
            begin
                if c_mul='1' or rst='1' then
                    mult_result <= (others=>'0');
                elsif rising_edge(clk) then
                    if l_mul = '1' then
                        mult_result <= std_logic_vector(signed(sub_result) * signed(sub_result));
                    end if; 
                end if;
            end process;

add_16b:process(clk,rst,c_add,l_add)
        begin
            if c_add='1' or rst='1' then
                reg_out_add19b <= (others=>'0');
            elsif rising_edge(clk) then
                if l_add = '1' then
                    reg_out_add19b <= std_logic_vector(signed(reg_out_add19b) + signed(mult_result));
                end if; 
            end if;
        end process;


div_8:process(clk,rst,c_div8,l_div8)
            begin
                if c_div8='1' or rst='1' then
                    sresult <= (others=>'0');
                elsif rising_edge(clk) then
                    if l_div8 = '1' then
                        sresult <= reg_out_add19b(18 downto 3);
                    end if;
                end if;
            end process;

result<=sresult;
lt8<=cnt_lt_8;
end Behavioral;
